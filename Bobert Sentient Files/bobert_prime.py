import sounddevice as sd
import numpy as np
import time
import random
from scipy.io import wavfile
from datetime import datetime
import threading
import RPi.GPIO as GPIO
import json
import os
import cv2
import uuid
import subprocess

SAMPLE_RATE = 16000
LISTEN_DURATION = 1  # seconds
SPEAK_DURATION = 1   # seconds

TERMINAL_LOG_PATH = "/media/Bobert/MEMORYBERT/logs/touchbert_cleaned_log.txt"
LEARNING_STATE_PATH = "/media/Bobert/MEMORYBERT/logs/learning_state.json"
LEARNING_LOG_PATH = "/media/Bobert/MEMORYBERT/logs/learning_log.json"

short_term_memory = []  # buffer of last few actions (max 10)

# === Logging Functions ===
def log_terminal_entry(entry):
    timestamp = datetime.utcnow().isoformat()
    with open(TERMINAL_LOG_PATH, "a") as log_file:
        log_file.write(f"{timestamp} | {entry}\n")

def get_best_move():
    memory_file = "/media/Bobert/MEMORYBERT/logs/movement_memory.json"
    try:
        with open(memory_file, "r") as f:
            memory = json.load(f)
    except:
        memory = []

    move_scores = {"left": 0, "right": 0, "forward": 0}
    for entry in memory:
        move = entry.get("move")
        reward = entry.get("reward", 0)
        if move in move_scores:
            move_scores[move] += reward

    best_move = max(move_scores, key=move_scores.get)
    return best_move

def capture_vision():
    img_name = f"cam_{uuid.uuid4().hex[:8]}.jpg"
    full_path = f"/media/Bobert/MEMORYBERT/logs/{img_name}"
    subprocess.run(["libcamera-still", "-n", "-o", full_path, "--width", "320", "--height", "240", "--timeout", "1"])
    return img_name

def log_vision_and_move(img, move):
    log_terminal_entry(f"vision={img} | move={move}")

    memory_file = "/media/Bobert/MEMORYBERT/logs/movement_memory.json"
    try:
        with open(memory_file, "r") as f:
            memory = json.load(f)
    except:
        memory = []

    memory.append({
        "vision": img,
        "move": move,
        "reward": 0
    })

    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

def load_learning_state():
    try:
        with open(LEARNING_STATE_PATH, "r") as f:
            return json.load(f)
    except:
        state = {"reward_points": 0, "punishment_points": 0, "last_updated": None}
        save_learning_state(state)
        return state

def save_learning_state(state):
    state["last_updated"] = datetime.utcnow().isoformat()
    with open(LEARNING_STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def save_learning_log():
    with open(LEARNING_LOG_PATH, "w") as f:
        json.dump(short_term_memory, f, indent=2)

learning_state = load_learning_state()

# === GPIO Setup ===
REWARD_PIN = 12
PUNISH_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(REWARD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PUNISH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

last_reward_time = 0
last_punish_time = 0
COOLDOWN = 5

def monitor_reinforcement():
    global last_reward_time, last_punish_time, learning_state, short_term_memory
    last_state_reward = GPIO.input(REWARD_PIN)
    last_state_punish = GPIO.input(PUNISH_PIN)
    while True:
        current_time = time.time()
        current_state_reward = GPIO.input(REWARD_PIN)
        current_state_punish = GPIO.input(PUNISH_PIN)

        log_terminal_entry(f"debug_gpio_state | reward_pin={current_state_reward} | punish_pin={current_state_punish}")

        if current_state_punish == GPIO.LOW and last_state_punish == GPIO.HIGH and (current_time - last_punish_time) > COOLDOWN:
            learning_state["punishment_points"] += 1
            if short_term_memory:
                short_term_memory[-1]["reinforcement"] = "negative"
                save_learning_log()
            save_learning_state(learning_state)
            log_terminal_entry("reinforcement=negative | punishment_points=" + str(learning_state["punishment_points"]))
            last_punish_time = current_time
            last_reward_time = current_time  # also lock reward cooldown

        elif current_state_reward == GPIO.LOW and last_state_reward == GPIO.HIGH and (current_time - last_reward_time) > COOLDOWN and current_state_punish == GPIO.HIGH:
            learning_state["reward_points"] += 1
            if short_term_memory:
                short_term_memory[-1]["reinforcement"] = "positive"
                save_learning_log()
            save_learning_state(learning_state)
            log_terminal_entry("reinforcement=positive | reward_points=" + str(learning_state["reward_points"]))
            last_reward_time = current_time
            last_punish_time = current_time  # also lock punish cooldown

        last_state_reward = current_state_reward
        last_state_punish = current_state_punish
        time.sleep(0.05)

reinforce_thread = threading.Thread(target=monitor_reinforcement, daemon=True)
reinforce_thread.start()

def listen(duration=LISTEN_DURATION):
    log_terminal_entry("status=starting_recording")
    recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    log_terminal_entry("status=recording_finished")
    return np.squeeze(recording)

def choose_to_speak():
    return random.random() < 0.5

def generate_audio_response(input_audio):
    start = random.randint(0, len(input_audio) - int(SAMPLE_RATE * SPEAK_DURATION))
    return input_audio[start:start + int(SAMPLE_RATE * SPEAK_DURATION)]

def play_audio(audio):
    sd.play(audio, samplerate=SAMPLE_RATE)
    sd.wait()

def log_interaction(input_audio, output_audio, spoke, move, img):
    timestamp = datetime.utcnow().isoformat().replace(":", "_").replace(".", "_")
    base_path = f"/media/Bobert/MEMORYBERT/logs/{timestamp}"
    input_path = f"{base_path}_input.wav"
    output_path = f"{base_path}_output.wav"

    wavfile.write(input_path, SAMPLE_RATE, (input_audio * 32767).astype(np.int16))

    if spoke:
        wavfile.write(output_path, SAMPLE_RATE, (output_audio * 32767).astype(np.int16))
        log_terminal_entry(f'spoke=true | input="{input_path}" | output="{output_path}" | move="{move}"')
    else:
        log_terminal_entry(f'spoke=false | input="{input_path}" | move="{move}"')

    # Save to short-term memory
    short_term_memory.append({
        "timestamp": timestamp,
        "input_file": input_path,
        "output_file": output_path if spoke else None,
        "spoke": spoke,
        "reinforcement": None,
        "saw": img
    })
    if len(short_term_memory) > 10:
        short_term_memory.pop(0)
    save_learning_log()

def summarize_state(input_audio):
    volume = np.mean(np.abs(input_audio))
    if volume > 0.2:
        emotion = "excited"
    elif volume > 0.05:
        emotion = "curious"
    else:
        emotion = "calm"
    state = f"emotion={emotion} | avg_volume={volume:.4f} | status=idle"
    log_terminal_entry(state)

cap = cv2.VideoCapture("libcamerasrc ! videoconvert ! appsink", cv2.CAP_GSTREAMER)

def bobert_loop():
    log_terminal_entry("Bobert Prime is online. Listening, thinking, maybe speaking.")
    while True:
        ret, frame = cap.read()
        if ret:
            pass

        move = get_best_move()
        img = capture_vision()
        log_vision_and_move(img, move)

        input_audio = listen()
        spoke = choose_to_speak()
        output_audio = generate_audio_response(input_audio) if spoke else np.zeros_like(input_audio)
        if spoke:
            play_audio(output_audio)
        log_interaction(input_audio, output_audio, spoke, move, img)
        summarize_state(input_audio)
        time.sleep(1)

if __name__ == "__main__":
    bobert_loop()

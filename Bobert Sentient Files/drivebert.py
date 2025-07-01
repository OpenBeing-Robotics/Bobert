import time, serial

log = "/media/Bobert/MEMORYBERT/logs/touchbert_cleaned_log.txt"
port = "/dev/ttyUSB0"
ser = serial.Serial(port, 9600)
last_cmd = ""

while True:
    try:
        with open(log) as f:
            lines = f.readlines()
        move_line = next((l for l in reversed(lines) if "move=" in l.lower()), "")
        if move_line:
            move = move_line.lower().split("move=")[-1].split()[0].strip()
            cmd = {"left":"l","forward":"f","right":"r","null":"n"}.get(move, "n")
            if cmd != last_cmd:
                ser.write(cmd.encode())
                last_cmd = cmd
        time.sleep(1)
    except Exception: pass

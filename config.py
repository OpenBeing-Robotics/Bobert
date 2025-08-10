"""
Configuration file for Bobert Robot
Set your API keys and configuration here
"""

import os
from pathlib import Path

# Base directory for logs and data
BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "logs"

# Create log directory if it doesn't exist
LOG_DIR.mkdir(exist_ok=True)

# API Configuration
# Set these environment variables or modify the defaults
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")
WEATHER_LOCATION = os.getenv("WEATHER_LOCATION", "London")

# Hardware Configuration
GPIO_PINS = {
    "left_motor_forward": 17,
    "left_motor_backward": 18,
    "right_motor_forward": 22,
    "right_motor_backward": 23,
    "reward_pin": 12,
    "punish_pin": 16
}

# Camera Configuration
CAMERA_INDEX = 0
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

# Audio Configuration
SAMPLE_RATE = 16000
LISTEN_DURATION = 1  # seconds
SPEAK_DURATION = 1   # seconds

# Serial Configuration
SERIAL_PORTS = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyACM0", "/dev/ttyACM1"]
SERIAL_BAUD_RATE = 9600

# Learning Configuration
MEMORY_BUFFER_SIZE = 10
REINFORCEMENT_COOLDOWN = 5  # seconds

# Robot Personality
DEFAULT_PERSONALITY = "Happy, helpful, mildly insane"

def validate_config():
    """Validate configuration and print warnings"""
    warnings = []
    
    if not OPENAI_API_KEY:
        warnings.append("OPENAI_API_KEY not set - AI responses will not work")
    
    if not OPENWEATHER_API_KEY:
        warnings.append("OPENWEATHER_API_KEY not set - Weather function will not work")
    
    if not NEWSAPI_KEY:
        warnings.append("NEWSAPI_KEY not set - News function will not work")
    
    if warnings:
        print("Configuration Warnings:")
        for warning in warnings:
            print(f"  ⚠️  {warning}")
        print("\nTo fix these warnings, set the appropriate environment variables:")
        print("export OPENAI_API_KEY='your_key_here'")
        print("export OPENWEATHER_API_KEY='your_key_here'")
        print("export NEWSAPI_KEY='your_key_here'")
        print("export WEATHER_LOCATION='your_city_here'")
    
    return len(warnings) == 0

if __name__ == "__main__":
    validate_config()
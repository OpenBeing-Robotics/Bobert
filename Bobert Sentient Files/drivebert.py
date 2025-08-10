import time
import serial
import os
import json

# Use relative paths and create directories if they don't exist
BASE_LOG_DIR = "logs"
LOG_FILE = os.path.join(BASE_LOG_DIR, "touchbert_cleaned_log.txt")

# Create log directory if it doesn't exist
os.makedirs(BASE_LOG_DIR, exist_ok=True)

# Serial port configuration with fallback
SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

def setup_serial():
    """Setup serial connection with error handling"""
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Serial connection established on {SERIAL_PORT}")
        return ser
    except serial.SerialException as e:
        print(f"Failed to connect to {SERIAL_PORT}: {e}")
        # Try alternative ports
        alternative_ports = ["/dev/ttyUSB1", "/dev/ttyACM0", "/dev/ttyACM1"]
        for port in alternative_ports:
            try:
                ser = serial.Serial(port, BAUD_RATE, timeout=1)
                print(f"Serial connection established on {port}")
                return ser
            except serial.SerialException:
                continue
        print("No serial ports available")
        return None

def read_log_file():
    """Read the log file with error handling"""
    try:
        if not os.path.exists(LOG_FILE):
            print(f"Log file {LOG_FILE} not found")
            return []
        
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()
        return lines
    except Exception as e:
        print(f"Error reading log file: {e}")
        return []

def parse_move_command(move_line):
    """Parse move command from log line"""
    try:
        if "move=" in move_line.lower():
            move = move_line.lower().split("move=")[-1].split()[0].strip()
            cmd_map = {"left": "l", "forward": "f", "right": "r", "null": "n"}
            return cmd_map.get(move, "n")
    except Exception as e:
        print(f"Error parsing move command: {e}")
    return "n"

def main():
    """Main drivebert loop"""
    ser = setup_serial()
    if ser is None:
        print("Drivebert cannot run without serial connection")
        return
    
    last_cmd = ""
    
    try:
        while True:
            try:
                lines = read_log_file()
                if lines:
                    # Find the most recent move command
                    move_line = next((l for l in reversed(lines) if "move=" in l.lower()), "")
                    if move_line:
                        cmd = parse_move_command(move_line)
                        if cmd != last_cmd and cmd != "n":
                            ser.write(cmd.encode())
                            last_cmd = cmd
                            print(f"Sent command: {cmd}")
                
                time.sleep(1)
            except Exception as e:
                print(f"Error in main loop: {e}")
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down Drivebert...")
    finally:
        if ser and ser.is_open:
            ser.close()
            print("Serial connection closed")

if __name__ == "__main__":
    main()

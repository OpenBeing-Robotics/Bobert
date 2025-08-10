#!/usr/bin/env python3
"""
Main entry point for Bobert Robot
This script validates configuration and runs the appropriate module
"""

import sys
import os
import signal
from pathlib import Path

# Add current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

try:
    import config
    from config import validate_config
except ImportError as e:
    print(f"Configuration error: {e}")
    print("Please ensure config.py exists and is properly configured")
    sys.exit(1)

def signal_handler(sig, frame):
    """Handle shutdown gracefully"""
    print('\nShutting down Bobert...')
    sys.exit(0)

def main():
    """Main entry point"""
    print("🤖 Bobert Robot Starting Up...")
    print("=" * 50)
    
    # Validate configuration
    if not validate_config():
        print("\n⚠️  Configuration has warnings but continuing...")
    
    print("\nAvailable Bobert modules:")
    print("1. Bobert Prime (Main AI Brain)")
    print("2. Drivebert (Movement Control)")
    print("3. Original Bobert (Legacy Mode)")
    print("4. Configuration Check")
    
    while True:
        try:
            choice = input("\nSelect module to run (1-4, or 'q' to quit): ").strip().lower()
            
            if choice == 'q':
                print("Goodbye!")
                break
            elif choice == '1':
                print("\n🚀 Starting Bobert Prime...")
                run_bobert_prime()
            elif choice == '2':
                print("\n🔄 Starting Drivebert...")
                run_drivebert()
            elif choice == '3':
                print("\n🔧 Starting Original Bobert...")
                run_original_bobert()
            elif choice == '4':
                print("\n⚙️  Checking Configuration...")
                validate_config()
            else:
                print("Invalid choice. Please select 1-4 or 'q' to quit.")
                
        except KeyboardInterrupt:
            print("\n\nShutting down...")
            break
        except Exception as e:
            print(f"Error: {e}")

def run_bobert_prime():
    """Run Bobert Prime module"""
    try:
        from Bobert_Sentient_Files.bobert_prime import bobert_loop
        bobert_loop()
    except ImportError as e:
        print(f"Failed to import Bobert Prime: {e}")
        print("Make sure all dependencies are installed")
    except Exception as e:
        print(f"Error running Bobert Prime: {e}")

def run_drivebert():
    """Run Drivebert module"""
    try:
        from Bobert_Sentient_Files.drivebert import main as drivebert_main
        drivebert_main()
    except ImportError as e:
        print(f"Failed to import Drivebert: {e}")
        print("Make sure all dependencies are installed")
    except Exception as e:
        print(f"Error running Drivebert: {e}")

def run_original_bobert():
    """Run Original Bobert module"""
    try:
        # Import and run the original Bobert code
        exec(open("Bobert Original Code").read())
    except FileNotFoundError:
        print("Original Bobert code file not found")
    except Exception as e:
        print(f"Error running Original Bobert: {e}")

if __name__ == "__main__":
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    # Check if we're on a Raspberry Pi
    if not os.path.exists("/proc/cpuinfo") or "BCM" not in open("/proc/cpuinfo").read():
        print("⚠️  Warning: This doesn't appear to be a Raspberry Pi")
        print("Some features (GPIO, camera) may not work properly")
        print("Continue anyway? (y/n): ", end="")
        if input().lower() != 'y':
            sys.exit(0)
    
    main()
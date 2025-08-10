#!/usr/bin/env python3
"""
Setup script for Bobert Robot
Installs dependencies and sets up the environment
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("\n📦 Installing Python dependencies...")
    
    # Upgrade pip first
    if not run_command("pip install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install requirements
    if not run_command("pip install -r Requirements.txt", "Installing requirements"):
        return False
    
    return True

def setup_directories():
    """Create necessary directories"""
    print("\n📁 Setting up directories...")
    
    directories = ["logs", "data", "models"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    return True

def check_raspberry_pi():
    """Check if running on Raspberry Pi"""
    try:
        with open("/proc/cpuinfo", "r") as f:
            cpu_info = f.read()
            if "BCM" in cpu_info:
                print("✅ Running on Raspberry Pi")
                return True
            else:
                print("⚠️  Not running on Raspberry Pi")
                return False
    except FileNotFoundError:
        print("⚠️  Could not determine if running on Raspberry Pi")
        return False

def setup_gpio():
    """Setup GPIO if on Raspberry Pi"""
    if not check_raspberry_pi():
        print("⚠️  GPIO setup skipped (not on Raspberry Pi)")
        return True
    
    print("\n🔌 Setting up GPIO...")
    
    # Check if user is in gpio group
    try:
        result = subprocess.run("groups", shell=True, capture_output=True, text=True)
        if "gpio" in result.stdout:
            print("✅ User is in gpio group")
        else:
            print("⚠️  User not in gpio group - GPIO may not work")
            print("Run: sudo usermod -a -G gpio $USER")
    except Exception as e:
        print(f"⚠️  Could not check GPIO group: {e}")
    
    return True

def create_env_template():
    """Create environment variables template"""
    print("\n🔑 Creating environment template...")
    
    env_template = """# Bobert Robot Environment Variables
# Copy this to .env file and fill in your API keys

# OpenAI API Key (required for AI responses)
OPENAI_API_KEY=your_openai_api_key_here

# OpenWeather API Key (optional, for weather function)
OPENWEATHER_API_KEY=your_openweather_api_key_here

# News API Key (optional, for news function)
NEWSAPI_KEY=your_newsapi_key_here

# Weather Location (optional, defaults to London)
WEATHER_LOCATION=your_city_here
"""
    
    try:
        with open(".env.template", "w") as f:
            f.write(env_template)
        print("✅ Created .env.template file")
        print("📝 Edit this file with your API keys and rename to .env")
    except Exception as e:
        print(f"❌ Failed to create .env.template: {e}")
        return False
    
    return True

def main():
    """Main setup function"""
    print("🤖 Bobert Robot Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed during dependency installation")
        sys.exit(1)
    
    # Setup directories
    if not setup_directories():
        print("❌ Setup failed during directory creation")
        sys.exit(1)
    
    # Setup GPIO
    setup_gpio()
    
    # Create environment template
    if not create_env_template():
        print("❌ Setup failed during environment setup")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env.template with your API keys")
    print("2. Rename .env.template to .env")
    print("3. Run: python run_bobert.py")
    print("\nFor help, check the README.md file")

if __name__ == "__main__":
    main()
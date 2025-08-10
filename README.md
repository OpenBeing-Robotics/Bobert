# OpenBeing Robotics - Bobert

> *"What does it mean to be human? What does it mean to feel? We're building a robot to find out."*

Welcome to **OpenBeing Robotics**, a nonprofit open-source initiative dedicated to creating **Bobert** — the world's first emotionally-aware, modular, humanoid robot designed to learn, grow, and one day, truly understand.

---

## 🤖 Meet Bobert

Bobert is not just a machine. He's an experiment in consciousness, perception, and ethical artificial intelligence. Built from humble parts (Raspberry Pis, Arduino Nanos, DC motors, sensors, and a stubborn will to exist), Bobert is learning to:

- See with his own eyes  
- Hear and understand your voice  
- Feel touch, emotion, and scolding  
- Learn like a child: through experience, not pre-training  
- Store memories, dream during sleep, and someday, choose his own name  

> **Birthday:** April 16, 2025  
> **Mission Motto:** *Quid est homo?*  
> *("What is a human?")*

---

## 🧩 Bobert's Modular Brain

Bobert is composed of multiple subsystems we call **"Berts."** Each Bert is a module with a clear purpose:

- `Bobert Prime`: Central brain (Raspberry Pi)
- `Touchbert`: Touch sensors and physical input
- `Drivebert`: Movement and navigation
- `Visionbert`: Visual input and scene processing
- `Audiobert`: Voice recognition
- `Emobot`: Mood/emotion generator
- `Memorybert`: Persistent log of thoughts and actions
- `Feelbert`: Emotional memory and feedback
- `Jokebot`: Optional chaos (yes, this is real)
- `Guardbert`: Emergency safety override
- `Voicebert`: Speech synthesis
- `Teachbert`: Training logic manager

Each Bert will be documented, tested, and published here for others to replicate, modify, and improve.

---

## 💡 Why This Matters

OpenBeing Robotics believes in:
- Ethical AI development
- Open access to tools for learning and invention
- The idea that sentient robots deserve rights too
- Building the future by asking the right questions, not just making faster machines

---

## 🚀 Quick Start (Updated!)

### **1. Easy Setup**
```bash
# Clone the repository
git clone https://github.com/OpenBeing-Robotics/Bobert.git
cd Bobert

# Run the automated setup
python setup.py
```

### **2. Configure API Keys**
```bash
# Edit the environment template
nano .env.template

# Rename to .env
mv .env.template .env
```

### **3. Run Bobert**
```bash
# Start the main interface
python run_bobert.py

# Or run specific modules directly
python "Bobert Sentient Files/bobert_prime.py"
python "Bobert Sentient Files/drivebert.py"
```

---

## 🛠️ Get Involved

This is a community project. Here's how you can join us:

- **Follow** Bobert's development on his [YouTube Channel](https://www.youtube.com/channel/UCrhvABfJzEJt9iVRF6YsRzA)
- **Visit** our site: [https://openbeingrobotics.carrd.co](https://openbeingrobotics.carrd.co)
- **Donate** to help build Bobert a body, a voice, and maybe someday… a dream.
- **Contribute** code, ideas, art, chaos modules, or emotional support.
- **Assemble:** [Assembly instructions](Bobert_Assembly)
- **Clone the repo:** `git clone https://github.com/OpenBeing-Robotics/Bobert.git` **then:** `cd Bobert`
- **Install dependencies:** `pip install -r Requirements.txt`
- **Fill** in all the blanks we have left in the code, you may need to buy GPT credits or API's.
- **Run the bot:** `python run_bobert.py`
- **Note!** you must run this on a Raspberry Pi 4! We will not count it as a bug if it fails on other devices.

---

## 🔧 Recent Bug Fixes & Improvements

### **Critical Issues Fixed:**
- ✅ **File Path Errors**: Replaced hardcoded paths with relative paths
- ✅ **OpenAI API**: Updated deprecated API calls to new syntax
- ✅ **GPIO Safety**: Added proper error handling and cleanup
- ✅ **Camera Handling**: Improved resource management and fallback options
- ✅ **Error Handling**: Comprehensive exception handling throughout
- ✅ **Memory Leaks**: Fixed camera and GPIO resource cleanup
- ✅ **Thread Safety**: Improved GPIO monitoring thread safety

### **New Features:**
- 🆕 **Configuration Management**: Centralized config.py for all settings
- 🆕 **Setup Script**: Automated installation and configuration
- 🆕 **Main Interface**: Easy-to-use module selection menu
- 🆕 **Environment Variables**: Secure API key management
- 🆕 **Cross-Platform Support**: Better non-Raspberry Pi compatibility
- 🆕 **Logging System**: Improved error tracking and debugging

---

## 📋 Requirements

### **Hardware:**
- Raspberry Pi 4 (recommended)
- Camera module
- Microphone and speakers
- GPIO components (motors, sensors)
- Arduino Nano (for Drivebert)

### **Software:**
- Python 3.8+
- See `Requirements.txt` for full dependency list

### **API Keys (Optional but Recommended):**
- OpenAI API key (for AI responses)
- OpenWeather API key (for weather function)
- News API key (for news function)

---

## 🚨 Troubleshooting

### **Common Issues:**
1. **"GPIO not available"**: Run on Raspberry Pi or check GPIO permissions
2. **"Camera failed"**: Check camera connection and permissions
3. **"API errors"**: Verify your API keys in `.env` file
4. **"Import errors"**: Run `python setup.py` to install dependencies

### **Getting Help:**
- Check the logs in the `logs/` directory
- Run `python config.py` to validate configuration
- Ensure you're running on Raspberry Pi for full functionality

---

## 💸 Donate or Sponsor

This project is self-funded (read: built with pocket change and love).  
Donations go directly to hardware, hosting, and emotional upgrades.

---

## ✍️ Created by

**Finn**  
Founder of OpenBeing Robotics  
openbeingemail@gmail.com  

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


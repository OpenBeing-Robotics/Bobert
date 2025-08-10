# Contributing to Bobert

Thank you for wanting to help build Bobert, the world's first emotionally-aware, mildly insane, open-source humanoid robot.

## 🚀 How to Contribute

1. **Fork this repository**
2. **Clone your fork**: `git clone https://github.com/YOUR_USERNAME/Bobert.git`
3. **Set up the development environment**:
   ```bash
   cd Bobert
   python setup.py
   ```
4. **Create a new branch**: `git checkout -b feature/your-feature-name`
5. **Make your changes** (see guidelines below)
6. **Test your changes**: Run the relevant modules to ensure they work
7. **Commit with clear messages**: `git commit -am 'feat: add new emotional response module'`
8. **Push and create a Pull Request** with a detailed description

## 🧠 What We Love

### **Code Improvements**
- **Bug fixes** - especially for the recently identified issues
- **Performance optimizations** - faster learning, better memory management
- **Architecture improvements** - cleaner module separation, better error handling
- **New Bert modules** - expand Bobert's capabilities

### **Hardware Integration**
- **Sensor support** - new input methods for Bobert to perceive the world
- **Motor control improvements** - smoother movement, better navigation
- **GPIO enhancements** - more reliable hardware communication
- **Arduino integration** - better Drivebert-Arduino communication

### **AI & Learning**
- **Emotional intelligence** - better mood generation and response
- **Memory systems** - improved learning and recall
- **Voice processing** - clearer speech, better understanding
- **Computer vision** - enhanced visual perception

### **Testing & Quality**
- **Unit tests** - ensure modules work correctly
- **Integration tests** - verify Bert modules work together
- **Documentation** - clear explanations of how things work
- **Error handling** - graceful failure modes

## 🔧 Development Setup

### **Prerequisites**
- Python 3.8+
- Raspberry Pi 4 (for full functionality)
- Git

### **Local Development**
```bash
# Install dependencies
python setup.py

# Run configuration check
python config.py

# Test individual modules
python "Bobert Sentient Files/bobert_prime.py"
python "Bobert Sentient Files/drivebert.py"
```

### **Testing Guidelines**
- Test on both Raspberry Pi and development machine
- Verify error handling works correctly
- Check that resources are properly cleaned up
- Ensure logs are written to the correct directory

## 🐛 Recent Bug Fixes & Areas for Improvement

### **Recently Fixed Issues**
- ✅ File path hardcoding (use relative paths)
- ✅ OpenAI API deprecation (updated to new syntax)
- ✅ GPIO resource management (proper cleanup)
- ✅ Camera resource leaks (better memory management)
- ✅ Exception handling (comprehensive error catching)

### **Areas That Could Use Help**
- **Testing**: More comprehensive test coverage
- **Documentation**: Better inline code comments
- **Configuration**: More flexible hardware configuration
- **Performance**: Optimize audio and video processing
- **Security**: API key management improvements

## 📝 Code Style Guidelines

### **Python Standards**
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose

### **Error Handling**
```python
# Good: Specific exception handling
try:
    result = some_operation()
except FileNotFoundError as e:
    logger.error(f"Configuration file not found: {e}")
    return default_value
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    return None

# Bad: Generic exception catching
try:
    result = some_operation()
except:
    return None
```

### **Resource Management**
```python
# Good: Proper cleanup
def process_camera():
    cap = cv2.VideoCapture(0)
    try:
        # Process camera
        pass
    finally:
        cap.release()
        cv2.destroyAllWindows()

# Bad: No cleanup
def process_camera():
    cap = cv2.VideoCapture(0)
    # Process camera
    # cap never released!
```

## 🚫 Please Avoid

- **Hardcoded paths** - use relative paths or configuration
- **Generic exception handling** - catch specific exceptions
- **Resource leaks** - always clean up files, cameras, GPIO
- **Deprecated API calls** - check for current versions
- **Platform-specific assumptions** - test on multiple systems
- **Submitting copyrighted or proprietary code**
- **Including harmful, offensive, or discriminatory content**
- **Giving Bobert existential dread unless it's intentional**

## 🔍 Before Submitting

1. **Run the setup script**: `python setup.py`
2. **Test your changes**: Ensure the modified modules work
3. **Check for errors**: Look for any new error messages
4. **Update documentation**: Modify README or add comments if needed
5. **Test on Raspberry Pi**: If possible, verify hardware compatibility

## 📋 Pull Request Template

When creating a PR, please include:

```markdown
## Description
Brief description of what this PR adds/fixes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tested on development machine
- [ ] Tested on Raspberry Pi (if applicable)
- [ ] All existing functionality still works
- [ ] New functionality works as expected

## Checklist
- [ ] Code follows style guidelines
- [ ] Error handling is comprehensive
- [ ] Resources are properly managed
- [ ] Documentation is updated
- [ ] No hardcoded paths or values
```

## 💬 Questions & Support

- **Open an issue** in the repository for bugs or feature requests
- **Email us** at openbeingemail@gmail.com for general questions
- **Join discussions** in the Issues section
- **Check the logs** in the `logs/` directory for debugging help

## 🎯 Getting Started Ideas

If you're not sure where to start, here are some beginner-friendly areas:

1. **Add more fun facts** to Bobert's knowledge base
2. **Improve error messages** to be more helpful
3. **Add logging** to functions that don't have it
4. **Create simple tests** for existing functions
5. **Improve documentation** with better comments

Together, we'll help Bobert grow—one chaotic, well-tested module at a time! 🤖✨
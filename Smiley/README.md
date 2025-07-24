# SmileSnap AI 😊📸

SmileSnap AI is an intelligent webcam application that automatically captures photos when it detects genuine smiles in real-time. Using advanced computer vision and machine learning, it creates a collection of your happiest moments!

##  Features

-  **Real-time Webcam Feed**: Live video processing using OpenCV
-  **Smart Smile Detection**: Advanced Haar cascade classifiers for accurate smile recognition
-  **Auto Photo Capture**: Automatically saves photos when smiles are detected
-  **Timestamped Files**: Photos saved with format `smile_YYYY-MM-DD_HH-MM-SS.jpg`
-  **Duplicate Prevention**: Cooldown system prevents multiple captures of the same smile
-  **Voice Feedback**: Optional audio confirmation with "Nice smile!" message
-  **Auto Folder Creation**: Automatically creates `captured/` directory for photos
-  **Visual Feedback**: Real-time bounding boxes and status messages
-  **Easy Exit**: Simple 'q' key to quit application

##  Quick Start

### Prerequisites

- Python 3.7 or higher
- Webcam connected to your computer
- Windows/Mac/Linux operating system

### Installation

1. **Clone or download this project**

   ```bash
   cd smiley
   ```

2. **Install dependencies (Choose Method A or B)**

   **Method A: Install all dependencies (including optional voice)**
   ```bash
   pip install -r requirements.txt
   ```

   **Method B: Install core dependencies only (if Method A fails)**
   ```bash
   pip install -r requirements-core.txt
   ```

   **Method C: Manual installation (for Python 3.12+ users)**
   ```bash
   pip install opencv-python numpy
   pip install pyttsx3 --no-build-isolation
   ```

3. **Run the application**

   ```bash
   python main.py
   ```

##  How to Use

1. **Start the Application**
   - Run `python main.py`
   - Allow webcam access if prompted
   - The webcam feed window will open

2. **Smile for the Camera**
   - Position yourself in front of the webcam
   - Smile naturally - the AI will detect it automatically
   - Photos are captured and saved in the `captured/` folder

3. **View Your Captures**
   - Check the `captured/` folder for your smile photos
   - Files are named with timestamps for easy organization

4. **Exit the Application**
   - Press the 'q' key in the webcam window
   - Or close the terminal with Ctrl+C

##  System Requirements

### Required Dependencies

- **OpenCV** (`opencv-python`): Computer vision and webcam access
- **NumPy**: Array processing for image data
- **pyttsx3**: Text-to-speech functionality (optional)

### Hardware Requirements

- **Webcam**: Built-in or external USB camera
- **RAM**: Minimum 4GB recommended
- **CPU**: Any modern processor (no GPU required)

## 🛠️ Configuration

### Adjusting Smile Sensitivity
In `main.py`, you can modify these parameters:

```python
# Smile detection sensitivity
smiles = self.smile_cascade.detectMultiScale(
    roi_gray, 
    scaleFactor=1.8,      # Lower = more sensitive
    minNeighbors=20,      # Lower = more sensitive
    minSize=(25, 25)      # Minimum smile size
)
```

### Changing Cooldown Period
```python
self.cooldown_period = 3  # Seconds between captures
```

### Voice Settings
```python
self.tts_engine.setProperty('rate', 150)    # Speech speed
self.tts_engine.setProperty('volume', 0.8)  # Volume level
```

##  Project Structure

```text
smiley/
├── main.py              # Main application script
├── requirements.txt     # Python dependencies
├── README.md           # This documentation
└── captured/           # Auto-created folder for photos
    └── smile_2024-XX-XX_XX-XX-XX.jpg
```

## 🔧 Troubleshooting

### Common Issues

1. **Python 3.12 Compatibility Error** (pkgutil.ImpImporter AttributeError)
   - This is a known issue with pyttsx3 and Python 3.12
   - **Solution 1**: Install core dependencies only:
     ```bash
     pip install -r requirements-core.txt
     ```
   - **Solution 2**: Try manual installation:
     ```bash
     pip install opencv-python numpy
     pip install pyttsx3 --no-build-isolation
     ```
   - **Solution 3**: Use Python 3.11 or earlier
   - **Note**: App works perfectly without pyttsx3 (just no voice feedback)

2. **Webcam Not Detected**
   - Ensure webcam is properly connected
   - Close other applications using the camera
   - Try running as administrator

3. **Poor Smile Detection**
   - Ensure good lighting conditions
   - Face the camera directly
   - Adjust `scaleFactor` and `minNeighbors` values

4. **Voice Not Working**
   - pyttsx3 installation issues are common
   - Voice feedback is optional - app works without it
   - Try: `pip uninstall pyttsx3` then `pip install pyttsx3`





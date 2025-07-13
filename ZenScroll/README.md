# ZenScroll - YouTube Shorts Auto-Scroller

ZenScroll is an automated YouTube Shorts viewer that automatically scrolls to the next video when the current one ends. Perfect for hands-free browsing of YouTube Shorts content.

## Features

- **Automatic Video Detection**: Detects when YouTube Shorts videos end
-**Auto-Scroll**: Automatically scrolls to the next Short
- **Hands-Free Browsing**: No manual interaction needed
-**Easy Stop**: Press Ctrl+C to stop the script anytime
- **Continuous Loop**: Runs indefinitely until manually stopped

## How It Works

1. Opens YouTube Shorts in a Chrome browser
2. Monitors video playback time and duration
3. When a video is about to end (0.5 seconds remaining), it automatically scrolls down
4. Continues this process for endless Short browsing

## Requirements

- Python 3.6+
- Chrome browser installed
- ChromeDriver (automatically handled by Selenium 4.6+)

## Installation

1. **Install Python dependencies:**

   ```bash
   pip install selenium
   ```

2. **Ensure Chrome is installed** on your system

## Usage

1. **Run the script:**

   ```bash
   python script.py
   ```

2. **The script will:**
   - Open a Chrome browser window
   - Navigate to YouTube Shorts
   - Start automatically scrolling through videos

3. **To stop the script:**
   - Press `Ctrl+C` in the terminal
   - Or close the browser window

## Configuration

The script includes these timing settings that can be adjusted if needed:

- **Page load wait**: 5 seconds (line 12)
- **Video load wait**: 2 seconds (line 16)
- **End threshold**: 0.5 seconds before video ends (line 25)
- **Check interval**: 1 second (line 27)

## Troubleshooting

### Common Issues

1. **ChromeDriver not found**
   - Ensure you have Chrome browser installed
   - Update to Selenium 4.6+ for automatic driver management

2. **Videos not loading**
   - Check your internet connection
   - Increase the initial wait time (line 12)

3. **Script not scrolling**
   - Some videos might not have proper duration metadata
   - Try refreshing the page or restarting the script

4. **Browser window closes unexpectedly**
   - Make sure not to manually interact with the browser while the script runs
   - Check for any Chrome updates

### Customization

You can modify the script behavior by adjusting these values:

```python
# Increase if videos load slowly
time.sleep(5)  # Page load wait

# Adjust video detection timing
if duration - current_time <= 0.5:  # End threshold
```

## Legal Notice

This tool is for educational and personal use only. Please respect YouTube's Terms of Service and use responsibly. The script simulates normal user behavior but should not be used to artificially inflate view counts or engage in any prohibited activities.

## Files

- `script.py` - Main automation script
- `README.md` - This documentation file


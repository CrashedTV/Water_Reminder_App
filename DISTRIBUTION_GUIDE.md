# Water Reminder App - Distribution Guide

## Essential Files:
- `water_reminder.py` - Main application
- `water_icon.ico` - App icon
- `README.md` - User instructions

## Distribution Options:

### Option 1: Standalone Executable (Recommended)
1. Run `create_exe.bat`
2. Send `dist/WaterReminder.exe` to client
3. Client double-clicks to run (no Python needed)

### Option 2: Python Package
1. Run `python client_installer.py`
2. Zip `WaterReminder_Client` folder
3. Client extracts and runs `setup.bat`

## Files Included:
- `create_exe.bat` - Creates standalone executable
- `client_installer.py` - Creates client package
- `create_icon.py` - Generates app icon
- `create_shortcut.py` - Creates desktop shortcut
- `requirements.txt` - Dependencies list
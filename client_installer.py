import os
import shutil
import subprocess
import sys

def create_client_package():
    print("Creating client distribution package...")
    
    # Create client folder
    client_dir = "WaterReminder_Client"
    if os.path.exists(client_dir):
        shutil.rmtree(client_dir)
    os.makedirs(client_dir)
    
    # Copy essential files
    files_to_copy = [
        "water_reminder.py",
        "water_icon.ico", 
        "README.md",
        "requirements.txt"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, client_dir)
    
    # Create client setup script
    setup_script = """@echo off
echo Setting up Water Reminder App...

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python from python.org
    pause
    exit /b 1
)

echo Installing dependencies...
pip install watchdog winshell pywin32 Pillow

echo Creating desktop shortcut...
python -c "
import os, winshell
from win32com.client import Dispatch
desktop = winshell.desktop()
path = os.path.join(desktop, 'Water Reminder.lnk')
target = 'pythonw.exe'
arguments = '\"' + os.path.join(os.getcwd(), 'water_reminder.py') + '\"'
wDir = os.getcwd()
icon = os.path.join(os.getcwd(), 'water_icon.ico')
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.Arguments = arguments
shortcut.WorkingDirectory = wDir
if os.path.exists(icon): shortcut.IconLocation = icon
shortcut.save()
print('Desktop shortcut created!')
"

echo.
echo Setup complete! 
echo Water Reminder shortcut created on desktop.
echo Double-click the shortcut to run the app.
pause
"""
    
    with open(os.path.join(client_dir, "setup.bat"), "w") as f:
        f.write(setup_script)
    
    # Create run script
    run_script = """@echo off
pythonw water_reminder.py
"""
    
    with open(os.path.join(client_dir, "run.bat"), "w") as f:
        f.write(run_script)
    
    print(f"Client package created in '{client_dir}' folder")
    print("\nTo distribute:")
    print("1. Zip the entire folder")
    print("2. Send to client")
    print("3. Client runs setup.bat once")

if __name__ == "__main__":
    create_client_package()
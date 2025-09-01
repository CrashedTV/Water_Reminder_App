import os
import winshell
from win32com.client import Dispatch

def create_desktop_shortcut():
    desktop = winshell.desktop()
    path = os.path.join(desktop, "Water Reminder.lnk")
    target = "pythonw.exe"
    arguments = '"' + os.path.join(os.getcwd(), "water_reminder.py") + '"'
    wDir = os.getcwd()
    icon = os.path.join(os.getcwd(), "water_icon.ico")
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.Arguments = arguments
    shortcut.WorkingDirectory = wDir
    if os.path.exists(icon):
        shortcut.IconLocation = icon
    shortcut.save()
    
    print(f"Desktop shortcut created: {path}")

if __name__ == "__main__":
    try:
        create_desktop_shortcut()
    except ImportError:
        print("Installing required packages...")
        os.system("pip install winshell pywin32")
        create_desktop_shortcut()
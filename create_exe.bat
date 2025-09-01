@echo off
echo Creating standalone executable...

echo Installing PyInstaller...
pip install pyinstaller

echo Building executable...
pyinstaller --onefile --windowed --icon=water_icon.ico --name="WaterReminder" --add-data="water_icon.ico;." water_reminder.py

echo.
echo Executable created in dist/ folder!
echo File: dist/WaterReminder.exe
echo.
echo This single file can be distributed to clients.
echo No Python installation required on client machines.
pause
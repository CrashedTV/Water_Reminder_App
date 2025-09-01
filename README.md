# 💧 Water Reminder App

A modern desktop application that helps you stay hydrated by sending regular water drinking reminders with audio alerts.

![Water Reminder](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🎨 **Modern Dark UI** - Clean, professional interface
- ⏰ **Customizable Intervals** - Set reminder time in minutes
- 🔊 **Audio Alerts** - Continuous beeping until acknowledged
- 🖥️ **Desktop Notifications** - Popup reminders that stay on top
- 🔄 **Auto-Reload** - Automatically updates when code changes
- 💧 **Custom Icon** - Beautiful water drop icon
- 🚀 **Easy Distribution** - Multiple deployment options

## 🚀 Quick Start

### Option 1: Run from Source
```bash
# Clone the repository
git clone https://github.com/yourusername/water-reminder-app.git
cd water-reminder-app

# Install dependencies
pip install -r requirements.txt

# Run the application
python water_reminder.py
```

### Option 2: Standalone Executable
```bash
# Create executable
create_exe.bat

# Run the generated executable
dist/WaterReminder.exe
```

## 📋 Requirements

- Python 3.7+
- Windows OS
- Dependencies listed in `requirements.txt`

## 🎯 Usage

1. **Set Interval**: Enter your preferred reminder interval (default: 30 minutes)
2. **Start Reminders**: Click the green "▶ Start Reminders" button
3. **Stay Hydrated**: When the alarm sounds, click "✓ I Drank Water" to stop it
4. **Stop Anytime**: Use the red "⏹ Stop Reminders" button to pause

## 📦 Distribution

### For End Users (No Python Required)
```bash
# Create standalone executable
create_exe.bat
# Share: dist/WaterReminder.exe
```

### For Developers (Python Required)
```bash
# Create client package
python client_installer.py
# Share: WaterReminder_Client.zip
```

## 🛠️ Development

### Project Structure
```
water-reminder-app/
├── water_reminder.py      # Main application
├── water_icon.ico         # App icon
├── requirements.txt       # Dependencies
├── create_exe.bat        # Executable builder
├── client_installer.py   # Client package creator
└── README.md             # This file
```

### Key Components
- **GUI Framework**: Tkinter with modern styling
- **Audio Alerts**: Windows `winsound` module
- **File Watching**: `watchdog` for auto-reload
- **Icon Generation**: PIL/Pillow for custom icons
- **Packaging**: PyInstaller for executables

## 🎨 Screenshots

*Main Interface*
- Clean dark theme with blue accents
- Simple interval setting
- Clear start/stop controls

*Alarm Window*
- Prominent red alert window
- Stays on top of all applications
- Easy acknowledgment button

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Icon design inspired by modern flat design principles
- Audio alerts using Windows system sounds

## 📞 Support

If you encounter any issues or have suggestions:
- Open an issue on GitHub
- Check the [DISTRIBUTION_GUIDE.md](DISTRIBUTION_GUIDE.md) for deployment help

---

**Stay hydrated! 💧** Remember to drink water regularly for better health and productivity.
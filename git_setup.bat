@echo off
echo Setting up Git repository for Water Reminder App...

echo Initializing Git repository...
git init

echo Adding all files...
git add .

echo Creating initial commit...
git commit -m "Initial commit: Water Reminder App with modern UI and audio alerts"

echo Creating main branch...
git branch -M main

echo.
echo Git repository setup complete!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub
echo 2. Copy the repository URL
echo 3. Run: git remote add origin YOUR_REPO_URL
echo 4. Run: git push -u origin main
echo.
pause
@echo off
pyinstaller --onedir --windowed --name=cdyCopy --icon=icon.ico --add-data "icon.png;." --add-data "config.ini;." main.py
pause
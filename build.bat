@echo off
pyinstaller --onedir --name=EasyCopy --icon=icon.ico --add-data "icon.png;." --add-data "config.ini;." main.py
pause
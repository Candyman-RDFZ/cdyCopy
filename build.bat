@echo off
pyinstaller --onedir --name=EasyCopy --icon=icon.ico --add-data "icon.png;icon.png" main.py
pause
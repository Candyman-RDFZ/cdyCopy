@echo off
pyinstaller --windowed --onedir --name=EasyCopy --icon=icon.ico --add-data "assets;assets" main.py
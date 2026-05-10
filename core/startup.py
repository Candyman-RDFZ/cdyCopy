from pathlib import Path
import sys, platform, getpass, os

class startupManager:
    def __init__(self, appName, scriptPath):
        self.appName = appName
        self.system = platform.system()
        self.scriptPath = Path(scriptPath).resolve()
        if getattr(sys, 'frozen', False):
            self.exec = sys.executable
        else:
            self.exec = str(Path(sys.executable).with_name("pythonw.exe"))

    def enable(self):
        if self.system == 'Windows':
            self._enable_windows()
        elif self.system == 'Darwin':
            self._enable_mac()
        elif self.system == 'Linux':
            self._enable_linux()
        else:
            return 'Err'
        
    def disable(self):
        if self.system == 'Windows':
            self._disable_windows()
    
    def _enable_windows(self):
        import winreg as reg

        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_SET_VALUE)
        if self.exec.endswith(('python.exe', 'pythonw.exe')):
            cmd = f'"{self.exec}" "{self.scriptPath}"'
        else:
            cmd = f'"{self.exec}"'
        reg.SetValueEx(key, self.appName, 0, reg.REG_SZ, cmd)
        reg.CloseKey(key)

    def _disable_windows(self):
        import winreg as reg
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_SET_VALUE)
        try:
            reg.DeleteValue(key, self.appName)
        except:
            pass
        reg.CloseKey(key)
    
    def _enable_mac():
        pass

    def _enable_linux():
        pass
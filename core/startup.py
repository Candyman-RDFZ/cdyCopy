from pathlib import Path
import sys, platform, getpass, os

class startupManager:
    def __init__(self, appName):
        self.appName = appName
        self.system = platform.system()
        self.scriptPath = Path(sys.argv[0]).resolve()
        self.exec = sys.executable

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
        pass
    
    def _enable_windows(self):
        import winreg as reg

        # key = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_SET_VALUE)
        if self.exec.endswith(('python.exe', 'pythonw.exe')):
            cmd = f'"{self.exec}" "{self.scriptPath}"'
        else:
            cmd = f'"{self.exec}"'
        print(cmd)
        # reg.SetValueEx(key, self.appName, 0, reg.REG_SZ, cmd)
        # reg.CloseKey(key)
    
    def _enable_mac():
        pass

    def _enable_linux():
        pass
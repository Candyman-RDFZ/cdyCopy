import sys, subprocess
from pathlib import Path

def re(mainScript):
    pythonw = str(Path(sys.executable).with_name("pythonw.exe"))
    if getattr(sys, 'frozen', False):
        subprocess.Popen([pythonw])
    else:
        subprocess.Popen([pythonw, str(mainScript)])
    sys.exit()
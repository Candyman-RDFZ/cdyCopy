from pathlib import Path
from configparser import ConfigParser

INIFILEPATH = str(Path(__file__).parents[1] / 'config.ini')

config = ConfigParser()
config.read(INIFILEPATH)

def writeConfig(section, key, value):
    try:
        config[section][key] = str(value)
        with open(INIFILEPATH, 'w') as f:
            config.write(f)
    except:
        return
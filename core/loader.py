from pathlib import Path
from configparser import ConfigParser

INIFILEPATH = str(Path(__file__).parents[1] / 'config.ini')

config = ConfigParser()
config.read(INIFILEPATH)

def getConfig(section, key):
    try:
        return config[section][key]
    except:
        return
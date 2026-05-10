from configparser import ConfigParser

class Configuration:
    def __init__(self, INIPATH):
        self.config = ConfigParser()
        self.config.read(INIPATH)
        self.INIPATH = INIPATH

    def getConfig(self, section, key):
        try:
            return self.config[section][key]
        except:
            return
        
    def writeConfig(self, section, key, value):
        try:
            self.config[section][key] = str(value)
            with open(self.INIPATH, 'w') as f:
                self.config.write(f)
        except:
            return
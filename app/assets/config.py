import configparser
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class parse:
    def __init__(self):
        self.config = None
    
    def get_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(dir_path + '/../../config.ini')
        return self.config
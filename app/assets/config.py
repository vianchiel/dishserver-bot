# Core Libraries
import configparser
import logging
import os

# Set Global Variables
dir_path = os.path.dirname(os.path.realpath(__file__))

class parse:
    def __init__(self):
        self.config = None
    
    def get_config(self):
        # Initiate config parser
        self.config = configparser.ConfigParser()

        # Designate config file path
        read_path = os.path.join(dir_path, '..', '..', 'config.ini')

        # Attempt to read config file
        try:
            self.config.read(read_path)
        except:
            logging.error("Error importing configurations.")
            return None
        
        return self.config

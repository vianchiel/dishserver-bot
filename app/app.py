# Core Libraries
import os

# Importing Assets
import assets.config as config

# Set Global Variables
dir_path = os.path.dirname(os.path.realpath(__file__))

# root application class
class DishWasher:
    # Initialise the class item with default variables and actions 
    def __init__(self):
        self.cur_config = None
        print("Application is starting.")

    # Starting to run the application acting as a controller
    def run(self):
        # Get Configurations
        self.cur_config = config.parse().get_config()
        self.cur_config_dscd = self.cur_config['discord.configs']

if __name__ == '__main__':
    app = DishWasher()
    app.run()
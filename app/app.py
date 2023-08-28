# Core Libraries
import os

# Importing Assets
import assets.config as config

# Set Global Variables
dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    # Get Configurations
    cur_config = config.parse().get_config()
    cur_config_dscd = cur_config['discord.configs']
    


if __name__ == '__main__':
    main()
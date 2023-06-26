import os
import sys
import yaml


def read_config(config_file: str):
    """ Reads config file and returns config data """
    with open(config_file, 'r') as file:
        config_data = yaml.safe_load(file)
    return config_data


def get_config_file() -> str:
    """ Returns the config file path """
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file = 'config_dev.yaml' if 'dev' in sys.argv else 'config.yaml'
    return os.path.join(current_directory, config_file)


def get_settings_path() -> str:
    """ Returns the settings path """
    return os.path.dirname(os.path.abspath(__file__))

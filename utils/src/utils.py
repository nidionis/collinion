import json
import os
import os
import json
import numpy as np

def get_config(config_name):
    """
    Load configuration from a JSON file.
    
    Args:
        config_name: Name of the configuration file without extension
    
    Returns:
        Dictionary containing configuration data
    """
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the utils directory
    utils_dir = os.path.dirname(current_dir)
    # Build the path to the config file
    config_path = os.path.join(utils_dir, "config", f"{config_name}.json")
    
    with open(config_path, 'r') as f:
        return json.load(f)
def get_config(name="config"):
    config_dir = os.path.join(os.path.dirname(__file__), f"../{name}")
    config_file = os.path.join(config_dir, f"{name}.json")
    os.makedirs(config_dir, exist_ok=True)
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

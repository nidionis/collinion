import json
import os

def get_config(name="config"):
    config_dir = os.path.join(os.path.dirname(__file__), f"../{name}")
    config_file = os.path.join(config_dir, f"{name}.json")
    os.makedirs(config_dir, exist_ok=True)
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

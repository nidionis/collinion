#!/usr/bin/env python3

import subprocess
import sys
import os
import platform

def get_pip_command():
    """Return the appropriate pip command based on the Python version"""
    if sys.version_info.major == 3:
        return "pip3"
    return "pip"

def install_requirements():
    """Install required packages from requirements.txt"""
    pip_cmd = get_pip_command()
    requirements_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
    
    print("Installing required dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", pip_cmd, "install", "-r", requirements_path])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

def check_pygame():
    """Check if pygame is installed"""
    try:
        import pygame
        print(f"Pygame {pygame.version.ver} is installed")
        return True
    except ImportError:
        print("Pygame is not installed")
        return False

if __name__ == "__main__":
    install_requirements()

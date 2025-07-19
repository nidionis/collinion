#!/usr/bin/env python3

import os
import argparse
import sys
import platform
import importlib.util

HELP_MSG = """
    At least run\n
        ./run\n
    in your terminal\n
    or open the rules.py file\n
 
    Controls:
    - UP/DOWN: Adjust simulation speed (auto-detects maximum)
    - P or F: Toggle performance display
    - R: Reset to default speed
    - Q/SPACE/RETURN: Quit
"""

def check_and_install_dependencies():
    try:
        import pygame
        return True
    except ImportError:
        pass
    installer_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "utils", "install_dependencies.py")
    if os.path.exists(installer_path):
        spec = importlib.util.spec_from_file_location("install_dependencies", installer_path)
        installer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(installer)
        # Run the installer
        success = installer.install_requirements()
        return success
    else:
        print(f"Warning: Dependency installer not found at {installer_path}")
        return False

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description=HELP_MSG)
    argparser.add_argument("-f", "--files", nargs='*', type=str, default=["rules.py"], help="can run from several files")
    argparser.add_argument("--zoom", type=int, default=15, help="pixel / cell")
    argparser.add_argument("--skip-install", action="store_true", help="Skip dependency installation")
    args = argparser.parse_args()
    
    # Check and install dependencies unless explicitly skipped
    if not args.skip_install:
        dependencies_ok = check_and_install_dependencies()
        if not dependencies_ok:
            print("Warning: Some dependencies may be missing. The game may not run correctly.")
            print("You can try installing dependencies manually with: pip install pygame")
            if not args.skip_install:
                print("Continuing in 3 seconds...")
                import time
                time.sleep(3)

    FILE_INTERPRETED = "utils/src/rules.py"
    
    for file in args.files:
        with open(file, 'r') as src, open(FILE_INTERPRETED, 'w') as dest:
            dest.write(src.read() + '\n')
            
    # Pass command line arguments to the simulation
    cmd = f"{sys.executable} utils/src/main.py"
    if args.zoom:
        cmd += f" --zoom {args.zoom}"
    
    print("Launching game...")
    os.system(cmd)


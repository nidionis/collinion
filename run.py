#!/usr/bin/env python3

import os
import argparse
import sys
import platform

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

argparser = argparse.ArgumentParser(description=HELP_MSG)
argparser.add_argument("-f", "--files", nargs='*', type=str, default=["rules.py"], help="can run from several files")
argparser.add_argument("--zoom", type=int, default=15, help="pixel / cell")
args = argparser.parse_args()

if __name__ == "__main__":
    FILE_INTERPRETED = "utils/src/rules.py"
    
    for file in args.files:
        with open(file, 'r') as src, open(FILE_INTERPRETED, 'w') as dest:
            dest.write(src.read() + '\n')
            
    # Pass command line arguments to the simulation
    cmd = f"{sys.executable} utils/src/main.py"
    if args.zoom:
        cmd += f" --zoom {args.zoom}"
    
    os.system(cmd)


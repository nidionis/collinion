#!/usr/bin/env python3

import os
import argparse
import sys
import platform

HELP_MSG = """
    At least run
        ./run
    in your terminal
    or open the rules.py file
    
    Quit pressing q
"""

argparser = argparse.ArgumentParser()
argparser.add_argument("-f", "--files", nargs='*', type=str, default=["rules.py"], help="rules file(s)")
args = argparser.parse_args()

if __name__ == "__main__":
    FILE_INTERPRETED = "utils/src/rules.py"
    
    for file in args.files:
        with open(file, 'r') as src, open(FILE_INTERPRETED, 'w') as dest:
            dest.write(src.read() + '\n')
    os.system(f"{sys.executable} utils/src/main.py")


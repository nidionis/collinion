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
 
    Quit pressing q
"""

argparser = argparse.ArgumentParser(description=HELP_MSG)
argparser.add_argument("-f", "--files", nargs='*', type=str, default=["rules.py"], help="can run from several files")
args = argparser.parse_args()

if __name__ == "__main__":
    FILE_INTERPRETED = "utils/src/rules.py"
    
    for file in args.files:
        with open(file, 'r') as src, open(FILE_INTERPRETED, 'a') as dest:
            dest.write(src.read() + '\n')
    os.system(f"{sys.executable} utils/src/main.py")


#!/usr/bin/python3

import os
import argparse
HELP_MSG="""
    At least run
        ./run
    in your terminal
    or open the rules.py file
    
    Quit pressing q
"""

argparser = argparse.ArgumentParser()
argparser.add_argument("-f", "--files", nargs='*' , type=str, default="rules.py", help="rules file(s)")
args = argparser.parse_args()

if __name__ == "__main__":
    FILE_INTERPRETED = "src/rules.py"
    os.system(f"echo > {FILE_INTERPRETED}")
    files = args.files
    if not isinstance(files, list):
        files = [files]
    for file in files:
        os.system(f"cat {file} >> {FILE_INTERPRETED}")
    os.system(f"python3 src/main.py")
#!/usr/bin/env python

import os
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("-f", type=str, default="rules.py", help="rules file")
args = argparser.parse_args()

if __name__ == "__main__":
    #copy rules file to src/rules.py
    os.system(f"cp {args.f} src/rules.py")
    os.system(f"python3 src/main.py")
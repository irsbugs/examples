#!/usr/bin/env python3
#
# prog_step_1.py
#
# Steps:
# 1. A python3 set of statements. Execution flows from line 1 to the last line.
#       Uses argparse command line interface module.
#
# To experiment with argparse, start this program using various command line 
# options:
# $ python3 prog_step_1.py
# $ python3 prog_step_1.py -d
# $ python3 prog_step_1.py --debug
# $ python3 prog_step_1.py -h
# $ python3 prog_step_1.py --help
# $ python3 prog_step_1.py -dh
# $ python3 prog_step_1.py -d -h
# $ python3 prog_step_1.py --debug --help
# $ python3 -m pdb prog_step_1.py -d  <-- Using python debugger module
#
# Note: The program implements two statements on a single line. E.g.
# if args.debug: print("About to do Stuff_1")
# This is not recommended, but it is handy for inserting code debugging lines.
#
# Ian Stewart. Hamilton Python User Group. CC0. 20 August 2017
#
# Importing
import sys
import argparse

# Constants and variables.
PROG_NAME = 'Program - Step 1'
debug = False

# Instantiate
parser = argparse.ArgumentParser(description=PROG_NAME)

print("Starting program:", PROG_NAME)

# Use argparse to support --debug flag, and provide --help.
parser.add_argument('-d', '--debug', 
                    action='store_true',
                    help='Provides information to help with debugging.')
# Instantiate
args = parser.parse_args()

if args.debug:
    print(args)
if args.debug:
    print(args.debug)

# Do stuff_1
if args.debug: print("About to do Stuff_1")
print("Stuff_1 has been completed.")

# Do stuff_2
if args.debug: print("About to do Stuff_2")
print("Stuff_2 has been completed.")

sys.exit("Program has finished.")

#!/usr/bin/env python3
#
# prog_step_2.py
#
# Steps:
# 1. A python3 set of statements. Execution flows from line 1 to the last line.
#       Uses argparse command line interface module.
# 2. Implement procedural programming, a subtype of imperative programming.
#       Based upon the concept of precedure calls, in which statements are
#       structured into procedures (also known as subroutines or functions.)
#
#       Note: Functional programming flow is determined by the return values
#       of functions.
#
# Ian Stewart. Hamilton Python User Group. CC0. 20 August 2017
#
# Importing
import sys
import argparse

# Constants and variables.
PROG_NAME = 'Program - Step 2'
debug = False

# Instantiate
parser = argparse.ArgumentParser(description=PROG_NAME)


def main():
    """Main function. Controls the flow of the program."""
    returned_string_1 = do_stuff_1()
    print(returned_string_1)
    returned_string_2 = do_stuff_2()
    print(returned_string_2)
    sys.exit("Program has finished.")


def do_stuff_1():
    """This is function 1 to do some stuff"""
    if args.debug: print("Got to do_stuff_1")
    return "Stuff_1 function completed OK."


def do_stuff_2():
    """This is function 2 to do some stuff"""
    if args.debug: print("Got to do_stuff_2")
    return "Stuff_2 function completed OK."


# Program start
if __name__ == "__main__":
    print("Starting program:", PROG_NAME)

    # Use argparse to support --debug flag.
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='Provides information to help with debugging.')
    # Instantiate
    args = parser.parse_args()

    if args.debug: print(args)
    if args.debug: print(args.debug)

    # Call the main function to control the program.
    main()

#!/usr/bin/env python3
#
import sys

_description_ = """
    Define a function to get data from the User at the command line.
    Use while True loop to ensure data is entered or data is of the desired
    type.
    Apply format() function to the input() function.
    Read the global constants TEXT and PROMPT rather than pass them to
    function.
    Simple flow programming. Calls one function.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_05_c.py

# Set constants
TEXT = "Input a floating point or integer value"
PROMPT = 1.23

print("Program {} has started...".format(sys.argv[0]))


def get_float_input():
    "Function to get a floating point value."
    while True:
        data = input("\n{} [{}]:".format(TEXT, PROMPT))
        if data == "":
            data = PROMPT
        try:
            data = float(data)
            return data
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue

value = get_float_input()
print("Valid data entered. Value: {}".format(value))
print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_05_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_05_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

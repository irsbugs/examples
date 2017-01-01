#!/usr/bin/env python3
#
import sys

_description_ = """
    Use input () function to get data from the User at the command line.
    Use while True loop to ensure data is entered or data is of the desired
    type.
    Apply format() function to the input() function.
    Simple flow programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_05_b.py

# Set constants
TEXT = "Input a floating point or integer value"
PROMPT = 2.1

print("Program {} has started...".format(sys.argv[0]))

while True:
    data = input("\n{} [{}]:".format(TEXT, PROMPT))
    if data == "":
        data = PROMPT
    try:
        data = float(data)
        break
    except ValueError as e:
        print("Value Error: {}".format(e))
        print("Please re-enter...")
        continue

print("Valid data entered. Value: {}".format(data))
print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_05_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_05_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

#!/usr/bin/env python3
#
import sys

_description_ = """
    Define a function to get data from the User at the command line.
    Use while True loop to ensure data is entered or data is of the desired
    type.
    Apply format() function to the input() function.
    Use variables to hold text and prompt strings and pass them to the
    function.
    Simple program flow. One function.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_05_d.py

# Set variables
text_string = "Input a floating point or integer value"
prompt_string = "3.21"

print("Program {} has started...".format(sys.argv[0]))


def get_float_input(text, prompt):
    "Function to get a floating point value."
    while True:
        data = input("\n{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            data = float(data)
            return data
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue

# Call function and pass text and prompt strings.
value = get_float_input(text_string, prompt_string)
print("Valid data entered. Value: {}".format(value))

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_05_d.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_05_d.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

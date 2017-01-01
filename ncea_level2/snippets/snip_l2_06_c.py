#!/usr/bin/env python3
#
import sys

_description_ = """
    Define a function to get data from the User at the command line.
    Use 'while True' loop to ensure data is entered or data is of the desired
    type. Get integer, positive integer, float.
    Apply format() function to the input() function.
    A main() function is defined to call the other functions.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_06_c.py


def main():
    """
    Main function that calls all the other functions.
    """
    value = get_integer_entry()
    print("Valid data entered. Integer Value: {}".format(value))
    value = get_positive_integer_entry()
    print("Valid data entered. Positive Integer Value: {}".format(value))
    value = get_float_entry()
    print("Valid data entered. Floating Point Value: {}".format(value))


def get_integer_entry(text="Input integer", prompt="0"):
    """
    Return an integer value from input on the console.
    An integer value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            return int(data)
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue


def get_positive_integer_entry(text="Input +ve or -ve integer", prompt="0"):
    """
    Return an absolute abs() integer value from input on the console.
    i.e. If a negative integer is entered it is converted to be positive.
    An integer value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            data = int(data)
            return abs(data)
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue


def get_float_entry(text="Input floating point or integer", prompt="0", ):
    """
    Return a floating point value from input on the console.
    A float value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            return float(data)
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue


if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    main()

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_06_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_06_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

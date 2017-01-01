#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Circle calculations. Enter the radius.
    Use functions to calculate circumference and area of the circle.
    Use math.pi
    Use a float input function.
    No formatting of the calculated values.
    Simple flow programming, but calling 3 x functions.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_07_e.py

# Define constants
TEXT = "Enter the radius"
PROMPT = 1.5

print("Program {} has started...".format(sys.argv[0]))


def get_float_entry(prompt="0", text="Input floating point value"):
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


def calculate_circumference(radius):
    "Calculate the circumference of the circle"
    circumference = 2 * math.pi * float(radius)
    return circumference


def calculate_area(radius):
    "Calculate the area of a the circle"
    area = math.pi * float(radius)**2
    return area


radius = get_float_entry(PROMPT, TEXT)
circumference = calculate_circumference(radius)
area = calculate_area(radius)

print("A circle with a radius of: {}".format(radius))
print("Has a circumference of: {}".format(circumference))
print("And an area of: {}".format(area))

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_07_e.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_07_e.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

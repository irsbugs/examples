#!/usr/bin/env python3
#
import sys

_description_ = """
    Floating point. Demonstration of adding 0.1
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_20_a.py

print()
print("As an example of a decimal that doesn't have an exact binary value")
print("1/10 = 0.1 in decimal.")
print("Python performs the division of 1 by 10 and stores this as a\n"
      "Binary64 floating point value. When Python is required to display\n"
      "this stored binary value then conversion to decimal and rounding\n"
      "is performed to display 0.1")
print("1/10 = {}".format(1 / 10))
print()

print("However on some occasions the slight descrepancies between binary\n"
      "values and their displayed decimal values may be observed...")
print("0.1 + 0.1 = {}".format(0.1 + 0.1))
print("0.1 + 0.1 + 0.1 = {}".format(0.1 + 0.1 + 0.1))
print("0.1 + 0.1 + 0.1 + 0.1 = {}".format(0.1 + 0.1 + 0.1 + 0.1))
print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
      .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1))
print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
      .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
      .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
      .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
      .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
      .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
print()

input("Press Enter key to end program")
sys.exit()

"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_20_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_20_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

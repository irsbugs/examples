#!/usr/bin/env python3
#
import sys

_description_ = """
    Continuing demonstration of large integers and integer operators.
    Addition +, Subtraction -, and Exponent **
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_19_a.py

print()
print("Really Big Numbers...")
print("10**1000000 is the integer 1 followed by one million zeros.")
print("Printing out this number at 80 characters per line and 66 lines\n"
      "per page, would require 190 pages of paper.")
print()
a = 10**1000000 + 3
print("a = 10**1000000 + 3")
b = 10**1000000
print("b = 10**1000000")
print()
print("Subtraction: \na - b = {}".format(a - b))

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_17_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_17_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

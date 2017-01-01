#!/usr/bin/env python3
#
import sys

_description_ = """
    Floating point. Demonstration Max positve value of float.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_20_c.py

print()
print()
print("Excessively large floats return inf for infinity.")

print("Maximum positive float until positive infinity...")
print("1.7976931348623156e+308 is {}".format(1.7976931348623157e+308))
print("1.7976931348623157e+308 is {}".format(1.7976931348623157e+308))
print("1.7976931348623158e+308 is {}".format(1.7976931348623158e+308))
print("1.7976931348623159e+308 is {}".format(1.7976931348623159e+308))
print("1.7976931348623160e+308 is {}".format(1.7976931348623160e+308))
print("1.7976931348623161e+308 is {}".format(1.7976931348623161e+308))

print()
print("Excessively large integer overflows the float() function")
print("Maximum positive integer **308 to float overload...")
try:
    print("float(1 * 10**308) is {}".format(float(1 * 10**308)))
except OverflowError as e:
    print("float(1 * 10**308) is OverflowError: {}".format(e))

try:
    print("float(2 * 10**308) is {}".format(float(2 * 10**308)))
except OverflowError as e:
    print("float(2 * 10**308) is OverflowError: {}".format(e))

print()
print("Maximum positive integer **307 to float overload...")

try:
    print("float(16 * 10**307) is {}".format(float(16 * 10**307)))
except OverflowError as e:
    print("float(16 * 10**307) is OverflowError: {}".format(e))
try:
    print("float(17 * 10**307) is {}".format(float(17 * 10**307)))
except OverflowError as e:
    print("float(17 * 10**307) is OverflowError: {}".format(e))
try:
    print("float(18 * 10**307) is {}".format(float(18 * 10**307)))
except OverflowError as e:
    print("float(18 * 10**307) is OverflowError: {}".format(e))
try:
    print("float(19 * 10**307) is {}".format(float(19 * 10**307)))
except OverflowError as e:
    print("float(19 * 10**307) is OverflowError: {}".format(e))

print()
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_20_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_20_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

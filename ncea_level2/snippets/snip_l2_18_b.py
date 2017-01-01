#!/usr/bin/env python3
#
import sys
_description_ = """
    Introduce the float type. Multiplying by a floating point decimal.
    Addition +, Multiplication *
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_18_b.py

print()
# Simlar calculations using integer, then using floating point...
print("Seconds in Julian year of 365 1/4 days (as integer) = {}\n"
      "(60 * 60 * 24 * 365) + (60 * 60 * 6)"
      .format((60 * 60 * 24 * 365) + (60 * 60 * 6)))
print("Type for {}: {}".format((60 * 60 * 24 * 365) + (60 * 60 * 6),
                               type((60 * 60 * 24 * 365) + (60 * 60 * 6))))

print("\nCalculations using the floating point data type...")
print("Seconds in Julian year of 365.25 days (as float) = {}\n"
      "(60 * 60 * 24 * 365.25)"
      .format(60 * 60 * 24 * 365.25))
print("Type for {}: {}".format(60 * 60 * 24 * 365.25,
                               type(60 * 60 * 24 * 365.25)))

print()
print("Distance light travels in one year = {} meters\n"
      "60 * 60 * 24 * 365.25 * 299792458"
      .format(60 * 60 * 24 * 365.25 * 299792458))
print()
print("Distance from Sun to Proxima Centauri = {} meters\n"
      "60 * 60 * 24 * 365.25 * 299792458 * 4.25"
      .format(60 * 60 * 24 * 365.25 * 299792458 * 4.25))

print()
print("Floating point value changed to base 10 exponential notation.")
a = (60 * 60 * 24 * 365.25 * 299792458 * 4.25)
print(a)
print("Using format(value, '.1f') function, removes the exponential\n"
      "and shows the value to 1 decimal place.")
print(format(60 * 60 * 24 * 365.25 * 299792458 * 4.25, '.1f'))

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_18_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_18_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

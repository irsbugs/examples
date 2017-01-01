#!/usr/bin/env python3
#
import sys

_description_ = """
    Floating point. Demonstration of 1/10, while is equal to 0.1 in decimal
    is in binary 0.00011 and then infinately recurring 0011.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_20_b.py

print()
# 1/10 in binary form repeats as 0011 sequence. 0.0001100110011...
print("1/10 converted to binary with varying levels of precision...")
print()
for precision in range(4, 61, 8):
    total = 0.0
    bin_string = "0.0"
    for exponent in range(precision):
        if exponent % 4 == 0 or exponent % 4 == 1:
            total = total + 0 / 2**(exponent + 2)
            bin_string = bin_string + "0"
        if exponent % 4 == 2 or exponent % 4 == 3:
            total = total + 1 / 2**(exponent + 2)
            bin_string = bin_string + "1"
    print("{: >2d} binary bits: {}".format(precision + 1, bin_string))
    print("Returned in decimal form: {: <19}"
          .format(total))

print()

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_20_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_20_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

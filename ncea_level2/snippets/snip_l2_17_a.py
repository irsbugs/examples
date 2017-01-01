#!/usr/bin/env python3
#
import sys

_description_ = """
    Demonstration of large integers and integer operators.
    Multiplication *, Exponent **, Addition +, and Modulus %
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_17_a.py

for i in range(2, 40):
    # print("i = " + str(i))
    number_string = ""
    number = 0
    for j in range(1, i):
        # Build the string 1, 12, 123, 1234, .... 12345678901234...
        number_string = number_string + str(j % 10)
        # if debug: print(number_string)

    number = int(number_string)

    if i > 1 and i <= 9:
        # i=2 = 1 * 9 + 2 = 11
        # i=9 = 12345678 * 9 + 9 = 111111111
        print("{} * 9 + {} = "
              .format(number, i % 10))
        print(number * 9 +
              (i % 10))

    if i > 29 and i <= 39:
        # i=30 =
        # 12345678901234567890123456789 * 9 + 10**21 + 10**11 + 10**1 + 0 =
        print("{} * 9 + 10**{} + 10**{} + 10**{} + {} = "
              .format(number, 21 + i % 10, 11 + i % 10, 1 + i % 10,
                      i % 10))
        print(number * 9 +
              10**(21 + i % 10) +
              10**(11 + i % 10) +
              10**(1 + i % 10) +
              (i % 10))

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_17_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_17_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

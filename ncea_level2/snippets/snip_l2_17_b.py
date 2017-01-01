#!/usr/bin/env python3
#
import sys
_description_ = """
    Continuing demonstration of large integers and integer operators.
    Multiplication *, Exponent **, Addition +
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_17_b.py

print("\nEvaluating the equation...")
print("12345678901234567890123456789012345678 * 9 + 10**30 + 10**20 + "
      "10**10 + 9")
print()
value_1 = int("12345678901234567890123456789012345678")
print("number as integer: {: >40}".format(value_1))
print()
value_2 = value_1 * 9
print("integer * 9      : {: >40}".format(value_2))

value_3 = 10**30
print("10**30           : {: >40}".format(value_3))

value_4 = 10**20
print("10**20           : {: >40}".format(value_4))

value_5 = 10**10
print("10**10           : {: >40}".format(value_5))

value_6 = 9
print("9                : {: >40}".format(value_6))

print("-" * 60)
print("Addition Total   : {: >40}"
      .format(value_2 + value_3 + value_4 + value_5 + value_6))
print("-" * 60)

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_17_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_17_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

#!/usr/bin/env python3
#
import sys
_description_ = """
    Continuing demonstration of large integers and integer operators.
    Integer Division //, and Modulo %
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_17_d.py

print()
print("Integer Division (//) ~ floor division and Modulo (%) ~ remainder")
print(" 4 // 2 = {} and  4 % 2 = {}" .format(4 // 2, 4 % 2))
print(" 5 // 2 = {} and  5 % 2 = {}" .format(5 // 2, 5 % 2))
print("11 // 4 = {} and 11 % 4 = {}" .format(11 // 4, 11 % 4))

print()
print(" -4 // 2 = {} and  -4 % 2 = {}" .format(-4 // 2, -4 % 2))
print(" -5 // 2 = {} and  -5 % 2 = {}" .format(-5 // 2, -5 % 2))
print("-11 // 4 = {} and -11 % 4 = {}" .format(-11 // 4, -11 % 4))

print()
print(" 4 // -2 = {} and  4 % -2 = {}" .format(4 // -2, 4 % -2))
print(" 5 // -2 = {} and  5 % -2 = {}" .format(5 // -2, 5 % -2))
print("11 // -4 = {} and 11 % -4 = {}" .format(11 // -4, 11 % -4))

print()
print(" -4 // -2 = {} and  -4 % -2 = {}" .format(-4 // -2, -4 % -2))
print(" -5 // -2 = {} and  -5 % -2 = {}" .format(-5 // -2, -5 % -2))
print("-11 // -4 = {} and -11 % -4 = {}" .format(-11 // -4, -11 % -4))
print()

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_17_d.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_17_d.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

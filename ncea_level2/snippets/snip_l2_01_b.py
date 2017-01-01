#!/usr/bin/env python3
#
import sys
import time

_description_ = """
    Import time and use sleep() for the amount of time in seconds specified
    by the constant 'S'.
    Uses .format() function with print().
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_01_b.py

print("Program {} has started...".format(sys.argv[0]))

# Set constant S for the time to sleep. Constants are always in upper case.
# Once the value of a constant is set it should never be changed.
S = 7

print("Program has started. It will now sleep for {} seconds...".format(S))

time.sleep(S)

print("Program has finished sleeping.")
print("End of program")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_01_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_01_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

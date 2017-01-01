#!/usr/bin/env python3
#
# Import sys for retrieving the name of the program and performing the exit()
import sys
import time

_description_ = """
    Import time and use sleep() for the the number of seconds of the 'delay'
    variable. The input() function is used to get the desired delay from the
    user.
    Uses .format() function with print().
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_01_d.py

print("Program {} has started...".format(sys.argv[0]))

# delay_in_seconds will become initialized as a string variable.
delay_in_seconds = input("Enter the time in seconds for program to sleep: ")

print("Program will now sleep for {} seconds..."
      .format(delay_in_seconds))

# delay_in_seconds must be converted from a string to a numeric value.
# Using float()
time.sleep(float(delay_in_seconds))

print("Program has finished sleeping.")
print("End of program")
input("Press Enter key to end program")
sys.exit()
"""
Note: If the user does not enter a numeric value that can be converted to a
float, then the program will fail.

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_01_d.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_01_d.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

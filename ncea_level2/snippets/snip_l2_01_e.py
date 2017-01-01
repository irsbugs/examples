#!/usr/bin/env python3
#
import sys
import time

_description_ = """
    Import time and use sleep() for the the number of seconds of the
    'DELAY_IN_SECS' constant.
    Define a function to perform the delay. Note that within the
    function it can use the DELAY_IN_SECS constant that was previously set
    outside of the function. i.e. The function does not require being passed
    the DELAY_IN_SEC constant.
    Uses .format() function with print().
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_01_e.py

# Define Constant
DELAY_IN_SECS = 4

print("Program {} has started...".format(sys.argv[0]))


def delay_function():
    "Function to pause the program. Returns a message."
    print("Program will now sleep for {} seconds...".format(DELAY_IN_SECS))
    time.sleep(DELAY_IN_SECS)
    return "Program has finished sleeping."

# Program starts here and calls the delay_function() which returns the message.
message = delay_function()
print(message)

print("End of program")
input("Press Enter key to end program")
sys.exit()
"""
Notes:
Directly underneath the def delay_function(): is the message "Function to pause
the program." This is a documentation string (docstring) that explains what the
function does. When you get help on this program the help utility can read
these docstrings.

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_01_e.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_01_e.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

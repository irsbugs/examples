#!/usr/bin/env python3
#
import sys
import time

_description_ = """
    Import time and sleep for one second to provide a countdown.
    Use for loop. Call a function to to print the countdown.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_03_c.py

print("Program {} has started...".format(sys.argv[0]))


def print_function(counter):
    "Print the countdown."
    if counter == 0:
        print("\t...we have liftoff...")
        return
    print("\t{} seconds to go...".format(counter))


# reversed(range(6)) will produce countdown values from 5 down to 0
for countdown in reversed(range(6)):
    print_function(countdown)
    time.sleep(1)

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_03_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_03_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

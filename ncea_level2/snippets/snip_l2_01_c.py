#!/usr/bin/env python3
#
import sys
import time

_description_ = """
    Import time and use sleep() for the the number of seconds of the 'DELAY'
    constant. DELAY is a more meaningful name to the constant than using the
    letter 'S'.
    Uses .format() function with print().
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_01_c.py

# Use a descriptive constant of DELAY rather than the letter "S".
DELAY = 10

print("Program {} has started...".format(sys.argv[0]))
print("Program will now sleep for {} seconds..."
      .format(DELAY))

time.sleep(DELAY)

print("Program has finished sleeping.")
print("End of program")

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_01_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_01_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

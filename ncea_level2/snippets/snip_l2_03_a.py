#!/usr/bin/env python3
#
import sys
import time

_description_ = """
    Import time and use sleep(1) for one second intervals to provide a
    countdown. Use a for loop. Need to subtract from 5 to countdown to 0.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_03_a.py

print("Program {} has started...".format(sys.argv[0]))

# range(6) will produce countdown values from 0 to 5
for countdown in range(6):
    print(5 - countdown)
    time.sleep(1)
print("...we have liftoff...")

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_03_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_03_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

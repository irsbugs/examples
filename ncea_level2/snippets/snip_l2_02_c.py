#!/usr/bin/env python3
#
import sys
import time

_description_ = """
    Import time and use sleep() for the number of seconds of the
    'DELAY_IN_SECS' constant.
    Use a function to log the start and end of the program to a logging file.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_02_c.py

# Initialize constants.
DELAY_IN_SECS = 5

print("Program {} has started...".format(sys.argv[0]))


def log_message(information):
    "Write a time stamp and information to the log file."
    with open("log_snip_l2_02_c", "a") as log_file:
        message = "{}: {}".format(time.asctime(), information)
        log_file.write(message + "\n")

log_message("Program started.")

print("Program will now sleep for {} seconds...".format(DELAY_IN_SECS))
time.sleep(DELAY_IN_SECS)
print("Program has finished sleeping.")

log_message("Program finished.")

print("End of program. Proceed with viewing the file log_snip_l2_02_c")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_02_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_02_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

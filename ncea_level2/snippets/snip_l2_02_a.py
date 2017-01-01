#!/usr/bin/env python3
#
import sys
import time
_description_ = """
    Import time and sleep for the number of seconds of the 'DELAY_IN_SECS'
    constant. Log the start and end of the program to a logging file.
    Use log_file = open(), log_file.write() and log_file.close()
    Simple flow programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_02_a.py

# Initialize constants.
DELAY_IN_SECS = 8

print("Program {} has started...".format(sys.argv[0]))

log_file = open("log_snip_l2_02_a", "a")
message = "{}: Program started".format(time.asctime())
log_file.writelines(message + "\n")
log_file.close()

print("Program will now sleep for {} seconds...".format(DELAY_IN_SECS))
time.sleep(DELAY_IN_SECS)
print("Program has finished sleeping.")

log_file = open("log_snip_l2_02_a", "a")
message = "{}: Program finished.".format(time.asctime())
log_file.write(message + "\n")
log_file.close()

print("End of program. Proceed with viewing the file log_snip_l2_02_a")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_02_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_02_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

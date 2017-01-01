# Import sys for retrieving the name of the program in list sys.argv[0]
import sys
# Import time an use the sleep() function to provide a delay in the program.
import time

_description_ = """
    Import time and use sleep() for 5 seconds.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_01_a.py

print("Program {} has started...".format(sys.argv[0]))

print("Program will now sleep for 5 seconds...")

time.sleep(5)  # Time in seconds

print("Program has finished sleeping.")
print("End of program")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_01_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_01_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

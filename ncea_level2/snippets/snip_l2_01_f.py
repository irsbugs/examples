#!/usr/bin/env python3
#
import sys
import time

_description_ = """
    Introduce procedural programming style.
    Use if __name__ == "__main__": to start the program and call the main()
    function.
    Uses .format() function with print().
    The first argument of the list sys.argv, i.e. sys.argv[0] is the programs
    name. i.e. snip_l2_01_e.py
    The time.sleep(5) provides a 5 second delay.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_01_e.py


def main():
    "The main function will perform a 5 seconds delay using sleep() function."
    print("Program will now sleep for 5 seconds...")

    time.sleep(5)  # Time in seconds

    print("Program has finished sleeping.")


if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    main()

    print("End of program")

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_01_f.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_01_f.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

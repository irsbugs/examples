#!/usr/bin/env python3
#
import sys

_description_ = """
    Use input () function to get data from the User at the command line.
    Use while True loop to ensure data is entered or data is of the desired
    type.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_05_a.py

print("Program {} has started...".format(sys.argv[0]))

# Input a string or hit return for the prompted colour of "Blue".
data = input("\nEnter your favourite colour [Blue]: ")
if data == "":
    data = "Blue"
print("Favourite colour is: {}".format(data))

# Input a string. If nothing is input then repeat the input query.
while True:
    data = input("\nEnter your name: ")
    if data == "":
        print("No data was entered. Please re-enter...")
        continue
    else:
        break
print("Your name is: {}".format(data))

# Input a numeric string. Try converting the string to a float. If it won't
# convert to a float, then repeat the input query.
while True:
    data = input("\nInput a numeric value [1.0]: ")
    if data == "":
        data = 1.0
    try:
        data = float(data)
        break
    except ValueError as e:
        print("Value Error: {}".format(e))
        print("Please re-enter...")
        continue
print("Valid data entered. Value: {}".format(data))

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_05_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_05_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

#!/usr/bin/env python3
#
import sys
_description_ = """
    Produce the Fibonacci series. Get integer for how many in the series to
    produce. As these are integers, they are accurately produced to infinite.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_16_a.py

# Get an integer value for the number of samples i.e. range.
iteration = input("Total number of samples in Fibonacci sequence:")

try:
    iteration = abs(int(iteration))
except:
    print("Invalid number of samples. Exiting...")
    sys.exit()

# Limit the max and min number of Fibonacci numbers
if iteration > 250:
    print("Limiting number of samples to 250 to allow display scroll back.")
    iteration = 250
if iteration < 3:
    iteration = 3

# Initialize the Fibonacci list with its first two values....
fibonacci_list = [0, 1]
while True:
    # Add the last two entries on the list and append the result.
    fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
    if len(fibonacci_list) == iteration:
        break
    else:
        continue

print("Fibonacci Numbers...")
for index, number in enumerate(fibonacci_list):
    print(number)

print()
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_16_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_16_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

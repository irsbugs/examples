#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime
    int(math.sqrt(integer_under_test))
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_21_a.py

start_prompt = 0
range_prompt = 100
prime_list = []

# Get start integer
start_integer = input("Input start integer [{}]: ".format(start_prompt))
if start_integer == "":
    start_integer = start_prompt
try:
    start_integer = abs(int(start_integer))
except:
    print("Invalid start integer: {}. Exiting".format(start_integer))
    sys.exit()

# Get the range of integers
range_integer = input("Input range [{}]: ".format(range_prompt))
if range_integer == "":
    range_integer = range_prompt
try:
    range_integer = abs(int(range_integer))
except:
    print("Invalid range integer: {}. Exiting".format(range_integer))
    sys.exit()

# Divide by every integer from 2 up to the square root of number under test.
# If all divisions result in never having a modulo of 0, then it is a prime.
for i in range(start_integer, start_integer + range_integer + 1):
    max_value = int(math.sqrt(i))
    # print("i: {}, max_value: {}".format(i, max_value))
    is_prime = True
    for j in range(2, max_value + 1):
        # print(i, j)
        if i % j == 0:
            # Is not a prime so stop doing any further testing on this integer.
            # print("i%j=? {} % {} = {}".format(i, j, i%j))
            is_prime = False
            break
        else:
            continue
    # Finished looping, if is_prime still True then must be a prime so append.
    if is_prime is True:
        # print(i)
        prime_list.append(i)

print(prime_list)
print("length of prime_list: {}".format(len(prime_list)))

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_21_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_21_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

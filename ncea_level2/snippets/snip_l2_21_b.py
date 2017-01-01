#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime
    int(math.sqrt(integer_under_test))
    Provide statistics and better listing.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_21_b.py

start_prompt = 0
range_prompt = 100
prime_list = []

start_integer = input("Input start integer [{}]: ".format(start_prompt))

if start_integer == "":
    start_integer = start_prompt

try:
    start_integer = int(start_integer)
except:
    print("Invalid start integer: {}. Exiting".format(start_integer))
    sys.exit()

range_integer = input("Input range [{}]: ".format(range_prompt))

if range_integer == "":
    range_integer = range_prompt

try:
    range_integer = int(range_integer)
except:
    print("Invalid range integer: {}. Exiting".format(range_integer))
    sys.exit()

for i in range(start_integer, start_integer + range_integer + 1):
    max_value = int(math.sqrt(i))
    is_prime = True
    for j in range(2, max_value + 1):
        if i % j == 0:
            is_prime = False
            break
        else:
            continue
    if is_prime is True:
        prime_list.append(i)

print("\n{} prime numbers in the range {} to {}, as follows..."
      .format(len(prime_list), start_integer, start_integer + range_integer))

for prime in prime_list:
    print("{: >20}".format(prime))

sum_of_prime = 0
for prime in prime_list:
    sum_of_prime = sum_of_prime + prime
print("The sum of the prime numbers is: {}".format(sum_of_prime))

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_21_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_21_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

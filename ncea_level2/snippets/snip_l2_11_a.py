#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Get integer entry as radius. Calculate circumference, surface area and
    volume of sphere. Use iteration and output data each loop.
    Simple programming flow.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_11_a.py

print("Program {} has started...".format(sys.argv[0]))

radius = input("Enter integer value for radius: ")
try:
    radius = abs(int(radius))
except:
    print("Invalid radius. Exiting...")
    sys.exit()

iteration = input("Enter integer value for number of iterations: ")
try:
    iteration = abs(int(iteration))
except:
    print("Invalid number for iteration. Exiting...")
    sys.exit()

print("\nDimensions for spheres")
print("{: <15}{: <15}{: <15}{: <15}"
      .format("Radius", "Circumference", "Surface Area", "Volume"))
print("-" * 53)
for i in range(radius, radius + iteration):
    circumference = 2 * math.pi * i
    surface = 4 * math.pi * i ** 2
    volume = 4 / 3 * math.pi * i ** 3

    print("{: <15g}{: <15g}{: <15g}{: <15g}"
          .format(i, circumference, surface, volume))
print("-" * 53)
print("\nEnd of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_11_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_11_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

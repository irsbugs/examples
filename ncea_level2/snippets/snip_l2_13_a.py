#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Get integer entry for litres. Calculate radius, diameter, and
    circumference in centimeters, of sphere holding this volume.
    Use iteration and output data for each loop.
    Simple programming flow.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_13_a.py

print("Program {} has started...".format(sys.argv[0]))

volume = input("Enter integer value of sphere in litres: ")
try:
    volume = abs(int(volume))
except:
    print("Invalid volume. Exiting...")
    sys.exit()

iteration = input("Enter integer value for number of iterations: ")
try:
    iteration = abs(int(iteration))
except:
    print("Invalid number for iteration. Exiting...")
    sys.exit()

print("\nDimensions for spheres holding different volumes")
print("{: <18}{: <18}{: <18}{: <18}".format("Volume(litres)", "Radius(cm)",
      "Diameter(cm)", "Circumference(cm)"))
print("-" * 71)

for i in range(volume, volume + iteration):
    # calculate_radius of sphere in cm based on volume in litres (1000cu.cm).
    # Algorithm: r = (3 * (volume / (4 * Pi)))^1/3 * 10
    radius = (3 * (i / (4 * math.pi))) ** (1 / 3) * 10
    diameter = 2 * radius
    circumference = 2 * math.pi * radius

    print("{: <18g}{: <18g}{: <18g}{: <18g}"
          .format(i, radius, diameter, circumference))
print("-" * 71)
print("\nEnd of program.")

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_13_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_13_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

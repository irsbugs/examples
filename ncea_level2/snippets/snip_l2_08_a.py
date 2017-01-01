#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Sphere calculations. Enter the radius.
    Calculate surface area and volume of a shpere.
    Use math.pi
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Sphere Formulas
    A = 4 Pi r**2
    V = 4/3 Pi r**3
    Simple flow programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_08_a.py

print("Program {} has started...".format(sys.argv[0]))

radius = input("Enter the radius of the sphere: ")

try:
    radius = float(radius)
except:
    print("Invalid radius value. Exiting...")
    sys.exit()

surface_area = 4 * math.pi * radius ** 2
volume = 4 / 3 * math.pi * radius ** 3

print("A sphere with a radius of: {:g}".format(radius))
print("Has a surface area of: {:g}".format(surface_area))
print("And a volume of: {:g}".format(volume))

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_08_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_08_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Cube calculations. Enter the length of an edge.
    Calculate surface area, volume and internal diagonal.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Cube algorithms
    surface = 6 * edge ^2
    volume = edge ^3
    diagonal through the space of the cube = square root 3 * edge
    Simple flow programming style
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_09_a.py

print("Program {} has started...".format(sys.argv[0]))

edge = input("Enter the length of the edge of a cube: ")

try:
    edge = float(edge)
except:
    print("Invalid edge value. Exiting...")
    sys.exit()

surface = 6 * edge ** 2
print("Cube Surface Area: {:g}".format(surface))

volume = edge ** 3
print("Cube Volume: {:g}".format(volume))

diagonal = math.sqrt(3) * edge
print("Cube Space Diagonal: {:g}".format(diagonal))

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_09_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_09_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

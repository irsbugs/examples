#!/usr/bin/env python3

import sys
import math

_description_ = """
    Based on the length of an edge of a tetrahedron provide the dimensions.
    Tetrahedron a = edge
    Volume = a^3/(6 sqrt(2)
    Area = sqrt(3) a^2
    Face Area = (sqrt(3)/4) a^2
    Height = sqrt(2/3) a
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_22_a.py

edge_prompt = 1

# Get start integer
edge = input("Input the length of a tetraheron edge [{}]: "
             .format(edge_prompt))
if not edge:
    edge = edge_prompt
try:
    edge = abs(float(edge))
except:
    print("Invalid edge integer: {}. Exiting".format(edge))
    sys.exit()

# Calculate tetrahedron
volume = edge**3 / 6 * math.sqrt(2)
total_area = math.sqrt(3) * edge**2
face_area = math.sqrt(3) / 4 * edge**2
height = math.sqrt(2 / 3) * edge

print()
print("A tetrahedron with an edge length of {:g}".format(edge))
print("has a volume of {:g}".format(volume))
print("a total surface area of {:g}".format(total_area))
print("a single face area of {:g}".format(face_area))
print("and a height of {:g}".format(height))
print()
input("Press Enter key to end program")
sys.exit()

"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_22_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_22_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

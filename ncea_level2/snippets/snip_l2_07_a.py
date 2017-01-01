import sys

_description_ = """
    Circle calculations. Enter the radius.
    Calculate circumference and area of the circle.
    Use 3.1415 within the calculations for value of Pi.
    Simple flow programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_07_a.py

print("Program {} has started...".format(sys.argv[0]))

radius = input("Enter the radius: ")

try:
    float(radius)
except:
    print("Radius is not integer or float. Exiting...")
    sys.exit()

circumference = 2 * 3.1415 * float(radius)
area = 3.1415 * float(radius)**2

print("A circle with a radius of: {}".format(radius))
print("Has a circumference of: {}".format(circumference))
print("And an area of: {}".format(area))

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_07_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_07_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

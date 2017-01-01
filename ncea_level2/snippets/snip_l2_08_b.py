#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Sphere calculations. Enter the radius.
    Calculate surface area and volume of a shpere.
    Use math.pi
    Use a float input function and functions to calculate surface area and
    volume.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Procedural programming style
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_08_b.py

# Define constants and variables
TEXT = "Enter the radius"
radius_prompt = 5
debug = False


def main(radius):
    "Main rountine for calculating sphere surface area and volume."
    if debug: print("Value of prompt radius: {}".format(radius))
    radius = get_float_entry(radius, TEXT)
    if debug: print("Value of radius used: {}".format(radius))
    surface_area, volume = calculate_sphere(radius)

    print("A sphere with a radius of: {:g}".format(radius))
    print("Has a surface area of: {:g}".format(surface_area))
    print("And a volume of: {:g}".format(volume))


def calculate_sphere(radius):
    """
    Calculate the surface area and volume of a sphere.
    A = 4 Pi r**2
    V = 4/3 Pi r**3
    """
    surface = 4 * math.pi * radius ** 2
    volume = 4 / 3 * math.pi * radius ** 3
    return surface, volume


def get_float_entry(prompt="0", text="Input floating point value"):
    """
    Return a floating point value from input on the console.
    A float value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]: ".format(text, prompt))
        if data == "":
            data = prompt
        try:
            return float(data)
        except ValueError as e:
            if debug: print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue


if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    print("Enable debugging with -d or --debug")
    print("E.g. python {} --debug".format(sys.argv[0]))
    print("Set radius prompt value -r= or --radius=")
    print("E.g. python {} --radius=5.2".format(sys.argv[0]))

    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        if "-r" in option:
            radius_prompt_list = sys.argv[index].split("=")
            if len(radius_prompt_list) > 1:
                radius_prompt = radius_prompt_list[1]

    main(radius_prompt)

    print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_08_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_08_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

#!/usr/bin/env python3
#
import sys
import math
_description_ = """
    Get integer entry for cubic meters. Use functions to calculate radius,
    diameter, and circumference in meters, of sphere holding this volume.
    Use iteration and output data for each loop.
    Procedural programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_12_b.py

# Variables
volume_prompt = 1
sample = 20
debug = False


def main(data=volume_prompt, sample=sample):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    if debug: print("Volume: {}, Samples: {}".format(data, sample))
    # Get a integer value for the radius.
    volume = get_integer_entry(data, text="Enter volume of sphere")

    # Get a integer value for the number of samples i.e. range.
    iteration = get_integer_entry(sample, text="Enter number of iterations")

    print("\nDimensions of spheres for holding different volumes")
    print("{: <18}{: <18}{: <18}{: <18}"
          .format("Volume(cu.m)", "Radius(m)", "Diameter(m)",
                  "Circumference(m)"))
    print("-" * 71)

    for i in range(volume, volume + iteration):
        radius, diameter, circumference = calculate_sphere_dimension(i)
        print("{: <18g}{: <18g}{: <18g}{: <18g}"
              .format(i, radius, diameter, circumference))
    print("-" * 71)


def get_integer_entry(prompt="0", text="Input integer value"):
    """
    Return an integer value from input on the console.
    An integer value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            return abs(int(data))
        except ValueError as e:
            if debug: print("Value Error: {}".format(e))
            continue


def calculate_sphere_dimension(volume):
    "Calculate sphere radius, diameter and circumference based on volume."
    radius = (3 * (volume / (4 * math.pi))) ** (1 / 3)
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    return radius, diameter, circumference


if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    print("Enable debugging with -d or --debug")
    print("E.g. python {} --debug".format(sys.argv[0]))
    print("Set volume prompt value -v= or --volume=")
    print("E.g. python {} --volume=5".format(sys.argv[0]))
    print("Set number of samples -s= or --samples=")
    print("E.g. python {} --samples=20".format(sys.argv[0]))
    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        if "-v" in option:
            volume_prompt_list = sys.argv[index].split("=")
            if len(volume_prompt_list) > 1:
                volume_prompt = volume_prompt_list[1]

        if "-s" in option:
            sample_list = sys.argv[index].split("=")
            if len(sample_list) > 1:
                sample = sample_list[1]

    main(volume_prompt, sample)

print("\nEnd of program.")

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_12_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_12_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Get integer entry as radius. Use functions to calculate diameter,
    circumference and area of circle. Use iteration and output data each loop.
    Procedural programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_10_b.py

# Variables
radius_prompt = 1
sample = 20
debug = False


def main(data=radius_prompt, sample=sample):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    if debug: print("Radius: {}, Samples: {}".format(data, sample))
    # Get a integer value for the radius.
    radius = get_integer_entry(data, text="Enter radius of the circle")

    # Get a integer value for the number of samples i.e. range.
    iteration = get_integer_entry(sample, text="Enter number of iterations")

    print("\n{: <15}{: <15}{: <15}{: <15}"
          .format("Radius", "Diameter", "Circumference", "Area"))
    print("-" * 53)

    for i in range(radius, radius + iteration):

        diameter, circumference, area = calculate_circle(i)

        print("{: <15g}{: <15g}{: <15g}{: <15g}"
              .format(i, diameter, circumference, area))
    print("-" * 53)


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


def calculate_circle(radius):
    "Calculate circle diameter, circumference and area."
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return diameter, circumference, area


if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    print("Enable debugging with -d or --debug")
    print("E.g. python {} --debug".format(sys.argv[0]))
    print("Set radius prompt value -r= or --radius=")
    print("E.g. python {} --radius=5".format(sys.argv[0]))
    print("Set number of samples -s= or --samples=")
    print("E.g. python {} --samples=20".format(sys.argv[0]))
    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        if "-r" in option:
            radius_prompt_list = sys.argv[index].split("=")
            if len(radius_prompt_list) > 1:
                radius_prompt = radius_prompt_list[1]

        if "-s" in option:
            sample_list = sys.argv[index].split("=")
            if len(sample_list) > 1:
                sample = sample_list[1]

    main(radius_prompt, sample)

print("\nEnd of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_10_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_10_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

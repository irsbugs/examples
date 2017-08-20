#!/usr/bin/env python3
#
# prog_step_4.py
#
# Steps:
# 1. A python3 set of statements. Execution flows from line 1 to the last line.
#       Uses argparse command line interface module.
# 2. Implement procedural programming, a subtype of imperative programming.
# 3. Change the program to retrieve a radius and calculate a circle
#       circumference and area using seperate functions.
# 4. Argparse enables radius to be entered at the command line and become
#       the radius prompt value.
#
# Ian Stewart. Hamilton Python User Group. CC0. 20 August 2017
#
# Importing
import sys
import argparse
import math

# Constants and variables.
PROG_NAME = 'Program - Step 4 - Circle'
debug = False
radius = 1

# Instantiate
parser = argparse.ArgumentParser(description=PROG_NAME)


def main(radius_prompt):
    """
    Main function. Controls the flow of the program.
    Output the information to the console.
    """
    if args.debug: print(radius_prompt, type(radius_prompt))
    radius = get_radius(radius_prompt)
    print("Radius:", radius)

    circumference = get_circle_circumference(radius)
    print("Circumference: {:.3f}".format(circumference))

    area = get_circle_area(radius)
    print("Area: {:.3f}".format(area))

    sys.exit("Program has finished.")


def get_radius(radius_prompt):
    """Get the radius."""
    while True:
        input_string = input("Enter the radius [{}]: ".format(radius_prompt))
        if args.debug: print(input_string)
        if not input_string:
            input_string = radius_prompt
        try:
            radius = float(input_string)
            break
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter the radius value...")
    return radius


def get_circle_circumference(radius):
    """Calculate the circumference of the circle"""
    circumference = 2 * math.pi * radius
    if args.debug: print("Radius:", radius, "Circumference:", circumference)
    return circumference


def get_circle_area(radius):
    """Calculate the area of the circle."""
    area = math.pi * radius ** 2
    if args.debug: print("Radius", radius, "Area:", area)
    return area


# Program start
if __name__ == "__main__":
    print("Starting program:", PROG_NAME)

    # Use argparse to support --debug flag.
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='Provides information to help with debugging.')

    parser.add_argument('-r', '--radius',
                        type=float,
                        help='Provide the prompting value for the radius.')
    # Instantiate
    args = parser.parse_args()

    if args.debug: print(args)
    if args.debug: print(args.debug)

    # Call the main function to control the program.
    if args.radius is not None:
        radius = args.radius
    main(radius)

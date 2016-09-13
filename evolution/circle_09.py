#!/usr/bin/env python3



DEFAULT_PROMPT = 10
import math
import sys

def input_radius(prompt):
    """Get User input from the console."""
    radius = input("Enter the radius of the circle [{}]: ".format(prompt))
    if radius == "":
        radius = prompt
    return float(radius)

def calculate_circle_area(radius):
    """Supplied with the radius, calculate the area of a circle."""
    area = math.pi * radius ** 2
    return area

if __name__ == "__main__":
    """Launch circle program."""
    prompt = DEFAULT_PROMPT
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
    radius = input_radius(prompt)
    circle_area = calculate_circle_area(radius)
    print(circle_area)
                                                                          


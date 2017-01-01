import sys
import math

_description_ = """
    Circle calculations. Enter the radius.
    Use one function to calculate circumference and area of the circle.
    Use math.pi
    Use a float input function.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Procedural programming style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_07_g.py

# Define constants and variables
TEXT = "Enter the radius"
radius_prompt = 5.2
debug = False


def main(radius):
    "Main rountine for calculating circle circumference and area."
    if debug: print("Value of prompt radius: {}".format(radius))
    radius = get_float_entry(radius, TEXT)
    if debug: print("Value of radius used: {}".format(radius))
    circumference, area = calculate_circle(radius)

    print("A circle with a radius of: {:g}".format(radius))
    print("Has a circumference of: {:g}".format(circumference))
    print("And an area of: {:g}".format(area))


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


def calculate_circle(radius):
    "Calculate the circumference and area of a circle"
    circumference = 2 * math.pi * float(radius)
    area = math.pi * float(radius)**2
    return circumference, area


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
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_07_g.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_07_g.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

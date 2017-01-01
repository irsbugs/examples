#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Bicycle pedding cadence and sprocket ratios to determine speeds in each
    gear using functions. Introduces list[] and for loop iterating over a list.
    Written in procedural programming style
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_19_b.py

debug = False

# Wheel diameter of ~ 0.318309m has 1 meter circumference. 1/pi
diameter = 0.67  # 1/math.pi
WHEEL_MIN = 0.3
WHEEL_MAX = 0.75

cadence = 60  # 60 to 80 normal riding. Racing: 70 up hills and 90 the flat.
CADENCE_MIN = 40
CADENCE_MAX = 120

front_sprocket = 50  # Crankset_teeth. Range 20 to 60 teeth.
FRONT_SPROCKET_MIN = 20
FRONT_SPROCKET_MAX = 60

rear_sprocket_list = [28, 24, 21, 18, 15, 13, 11]  # Shimano 7-speed CS-HG70 ac


def main(diameter=diameter, cadence=cadence, front_sprocket=front_sprocket):
    """
    Main function that calls all other defined functions and statements.
    """

    if debug: print("Program is starting...")

    # Get diameter and if value is outside of min or max force value into range
    diameter = get_float_entry(diameter,
                               "Enter wheel diameter. Range {} to {} meters"
                               .format(WHEEL_MIN, WHEEL_MAX))
    if diameter < WHEEL_MIN:
        diameter = WHEEL_MIN
    if diameter > WHEEL_MAX:
        diameter = WHEEL_MAX
    if debug: print("Diameter of wheel in meters: {}".format(diameter))

    # Get cadence and if value is outside of min or max force value into range
    cadence = get_integer_entry(cadence, text="Pedalling cadence. "
                                "Revolutions per minute")
    if cadence < CADENCE_MIN:
        cadence = CADENCE_MIN
    if cadence > CADENCE_MAX:
        cadence = CADENCE_MAX
    if debug: print("Pedalling Cadence: {}".format(cadence))

    # Get sprocket and if value is outside of min or max force value into range
    front_sprocket = get_integer_entry(front_sprocket,
                                       text="Teeth on front sprocket")
    if front_sprocket < FRONT_SPROCKET_MIN:
        front_sprocket = FRONT_SPROCKET_MIN
    if front_sprocket > FRONT_SPROCKET_MAX:
        front_sprocket = FRONT_SPROCKET_MAX
    if debug: print("Teeth on front sprocket: {}".format(front_sprocket))

    # Provide statistics - Circumference. Revolutions for 1km
    # Revolutions per minute for 1km/hour
    circumference = diameter * math.pi
    print("\nInformation:")
    print("Wheel diameter: {:.3f}".format(diameter))
    print("Wheel circumference: {:.3f}".format(circumference))
    print("Revolutions to do 1km: {:.3f}".format(1000 / circumference))
    print("Revolutions per minute to do 1km in 1 hour: {:.3f}"
          .format(1000 / circumference / 60))

    # Provide rear cassette statistics.
    print("\nStatistics for each gear:")
    print("Cadence: {}".format(cadence))
    print("Gear  Teeth  Front:Back  Ratio   RPM       Km/h")
    print("-" * 50)
    for index, teeth in enumerate(rear_sprocket_list):
        ratio = front_sprocket / teeth
        wheel_rpm = cadence * ratio
        meter_per_minute = circumference * wheel_rpm
        meter_per_hour = meter_per_minute * 60
        kilometer_per_hour = meter_per_hour / 1000

        print("{: >2}{: >7}{: >9}:{: <2}{: >9.2f}{: >9.1f}{: >9.1f}"
              .format(index + 1, teeth, front_sprocket, teeth, ratio,
                      wheel_rpm, kilometer_per_hour))
    print("-" * 50)

    if debug: print("\nProgram is finished.")


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
            return int(data)
        except ValueError as e:
            if debug: print("Value Error: {}".format(e))
            continue


def get_float_entry(prompt="0", text="Input floating point value"):
    """
    Return a floating point value from input on the console.
    A float value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            return float(data)
        except ValueError as e:
            if debug: print("Value Error: {}".format(e))
            continue


def select_argument(index):
    """
    Select a value, if present, from a cli option with '=' delimiter.
    "E.g. --stuff=something, then select 'something', else return None.
    """
    option_list = sys.argv[index].split("=")
    if len(option_list) > 1:
        return option_list[1]
    else:
        return None


if __name__ == "__main__":
    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):

        if "-d" in option:
            debug = not debug

        if "-w" in option:
            if select_argument(index) is not None:
                diameter = select_argument(index)

        if "-s" in option:
            if select_argument(index) is not None:
                front_sprocket = select_argument(index)

        if "-c" in option:
            if select_argument(index) is not None:
                cadence = select_argument(index)

    if debug: print("sys.argv list = {}".format(sys.argv))
    if debug: print("Variables: debug:{}, diameter:{}, cadence:{}, "
                    "front sprocket:{}"
                    .format(debug, diameter, cadence, front_sprocket))

    # Call main program, pass values from command line arguments, or variables
    # with their default values which may not have been modified by the cli.
    main(diameter, cadence, front_sprocket)

    input("Press Enter key to end program")
    sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_19_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_19_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

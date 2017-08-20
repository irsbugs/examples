#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Bike_Speed. template_l2_19.py based on template_master_l2.py
# Introduces: Floating point calculations.
#       Determine the speed of a bicycle. Parameters that may be adjusted
#       are: Diameter of the rear wheel, Cadence (the revolutions per
#       minute of the pedalling and the Crankset teeth (Number of teeth
#       on the front sprocket).A list is provided for the number of teeth
#       on each sprocket of the casette on the rear wheel.
#       Integers are input, however calculations tend to be floats.
#
#
# TODO: Describe your program here so that its description will be displayed
# using help(). See pydocs https://docs.python.org/3/library/pydoc.html
# E.g. $ pydoc3 -p 1234 then in a browser http://localhost:1234/
#

# Template functions utilize modules. Import them now to avoid problems later.
# import modules    # Functions, St trings, Lists used in template:
import sys          # .version(), .hexversion(), .exit(), .argv .stdout.write()
#                   # .stdout.flush()
import os           # .sep, .getcwd()
import datetime     # .datetime.now().strftime() .datetime.utcnow().strftime()
#                   # .datetime.today()
import textwrap     # .TextWrapper()
import tempfile     # .TemporaryFile(), .gettempdir()
import time         # .time(), .sleep()
import locale       # .setlocale(), .currency()

# Modules that could be handy...
import decimal
import math
import random

# Program details variables.
_program_ = "Bike_Speed"  # "template_l2_08.py"
_version_ = "1.0"
_date_ = "2016-10-25"
_author_ = "Ian Stewart"
_copyright_ = "© https://creativecommons.org/licenses/by/4.0/"
_description_ = ("Determine the speed of a bicycle. Parameters that may be\n"
                 "adjusted are:\n"
                 "1. Diameter of the rear wheel.\n"
                 "2. Cadence. The revolutions per minute of the pedalling.\n"
                 "3. Crankset teeth. Number of teeth on the front sprocket.\n"
                 "A list provides the number of teeth on each sprocket of\n"
                 "the casette on the rear wheel.\n"
                 "Input values are Integers. Calculations are mostly floats.")
_original_ = ("template_master_l2.py - Ian Stewart - October 2016.\n"
              "© https://creativecommons.org/licenses/by/4.0/")

# Global Constants and variables init values. Can be read within functions.
# Can be the default values for arguments of a function.
PYTHON_MIN_VERSION = "3.2"
debug = False
log = "log_{}.txt".format(_program_)
radius = 1


MILLIMETER2METER = 0.001

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

input_file = "./temp/some_data.txt"
output_file = "./temp/some_data.txt"
timer_activated = 0

# Global variables that could be handy...
sep = os.sep
cwd = os.getcwd() + sep

# Check python is not below version 3. Prohibit running version 2.
if int(sys.version[:1]) < 3:
    print("Python version {} is not supported. \n"
          "Please restart using Python version 3 or higher. Exiting..."
          .format(sys.version.split(" ")[0]))
    sys.exit()


def main(diameter=diameter, cadence=cadence, front_sprocket=front_sprocket,
         log=log, in_file=input_file, out_file=output_file):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    message = "Program {} launched.".format(sys.argv[0])
    append_logfile(message, log)

    if debug: print("Program is starting...")
    # if debug: print("data: {}, logfile: {}".format(data, log))
    # if debug: print("in_file: {}, out_file: {}".format(in_file, out_file))
    #
    # Call functions here...
    print("{} is executing...".format(_program_))

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

    append_logfile("Wheel:{:g}, Cadence:{:g}, Sprocket:{:g}"
                   .format(diameter, cadence, front_sprocket))

    if debug: print("Program is finished.")
    append_logfile("Program {} finished.".format(_program_))
    input("\nPress Enter key to end program.")
    sys.exit()
    # ===== end of main function =====


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


def python_version_check():
    """
    Check the version of python used is at the minimum or above the value for
    PYTHON_MIN_VERSION.
    sys.hexversion are: aa (major) bb (minor) cc (micro) f0 (final release)
    E.g. 0xaabbccf0. 0x30502f0 is 3.5.2 (final release)
    """
    min_version_list = PYTHON_MIN_VERSION.split(".")
    # Truncate if the list is more the 4 items
    if len(min_version_list) > 4:
        min_version_list = min_version_list[:4]
    # Fill if the list is less then 4 items
    if len(min_version_list) == 1:
        min_version_list.append("0")
    if len(min_version_list) == 2:
        min_version_list.append("0")
    if len(min_version_list) == 3:
        min_version_list.append("f0")
    # Calculate the minimum version and an integer, which, when displayed as
    # hex, is easily recognised as the version. E.g. 0x30502f0 is 3.5.2
    min_version_value = 0
    for index, item in enumerate(min_version_list[::-1]):
        min_version_value = min_version_value + int(item, 16) * 2**(index * 8)
    if debug: print("Python Version Minimum:{}, Decimal:{}, Hex:{}"
                    .format(PYTHON_MIN_VERSION, min_version_value,
                            hex(min_version_value)))
    # test value and exit if below minimum revision
    if sys.hexversion < min_version_value:
        print("Python Version: {}. Required minimum version is: {}. Exiting..."
              .format(sys.version.split(" ")[0], PYTHON_MIN_VERSION))
        sys.exit()


def append_logfile(message=None, logfile=log, path=cwd):
    """
    Append a time stamp and message to a log file.
    Default to using the current working directory (cwd)
    Prefix with a time stamp.
    Example: 2016-10-18 10:37:38.306: A message
    If message exceeds 55 characters, then use textwrap to indent next line
    Uses: datetime
          textwrap
    """
    if message is None:
        return
    # Wrap the text if it is greater than 80 - 25 = 55 characters.
    # Indent 25 spaces to on left to allow for width of time stamp
    wrapper = textwrap.TextWrapper()
    wrapper.initial_indent = " " * 25
    wrapper.subsequent_indent = " " * 25
    wrapper.width = 80
    message = wrapper.fill(message).lstrip()

    if debug: print(path + logfile)
    f = open(path + logfile, "a")
    # Truncate the 6 digit microseconds to be 3 digits of milli-seconds
    stamp = ("{0:%Y-%m-%d %H:%M:%S}.{1}:".format(datetime.datetime.now(),
             datetime.datetime.now().strftime("%f")[:-3]))
    if debug: print(stamp + " " + message)
    f.write(stamp + " " + message + "\n")


def help():
    "Provide help on command line options available."
    print("Program: {0}, Version: {1}, Date: {2}, Author: {3}"
          .format(_program_, _version_, _date_, _author_))
    print("{}".format(_description_))
    print("Usage: {} [OPTION]".format(_program_))
    print("Arguments...")
    print("  -c=, --cadence=[VALUE]     Pedalling speed. Revolutions per min.")
    print("  -s=, --sprocket=[VALUE]    Teeth on the crankset sprocket")
    print("  -w=, --wheel=[VALUE]       Diameter of rear wheel.")
    print("  -h,  --help                Provide this help information.")
    print("  -d,  --debug               Provide additional information \n"
          "                             during program development.")
    # print("  -i=, --input=[FILE]        Input file")
    # print("  -o=, --output=[FILE]       Output file")
    # print("  -s=, --stuff=[VALUE]       Assign a value to stuff")
    print("  -l=, --log=[FILE]          Provide a filename for logging.")
    print("")
    print("Copyright: {}\n".format(_copyright_))


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
        if "-h" in option:
            help()
            sys.exit()

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        # Overide "stuff" global variable.
        # Use = as the delimiter to split keyword and value. E.g.
        # -s=1, --stuff=2, -s="  Has spaces  ", --stuff=Smith, -s=4=four, etc.

        if "-w" in option:
            if select_argument(index) is not None:
                diameter = select_argument(index)

        if "-s" in option:
            if select_argument(index) is not None:
                front_sprocket = select_argument(index)

        if "-c" in option:
            if select_argument(index) is not None:
                cadence = select_argument(index)

        if "-r" in option:
            radius_list = sys.argv[index].split("=")
            if len(radius_list) > 1:
                radius = radius_list[1]

        if "-i" in option:
            input_list = sys.argv[index].split("=")
            if len(input_list) > 1:
                input_file = input_list[1]

        if "-o" in option:
            output_list = sys.argv[index].split("=")
            if len(output_list) > 1:
                output_file = output_list[1]

        # Provide for a log file. Changes file name assigned to "log" variable.
        if "-l" in option:
            log_list = sys.argv[index].split("=")
            if len(log_list) > 1:
                # Avoid complexity of log file in sub-directories. In cwd.
                if os.sep not in log_list[1]:
                    log = log_list[1]

    if debug: print("sys.argv list = {}".format(sys.argv))
    if debug: print("Variables: debug:{}, diameter:{}, cadence:{}, "
                    "log:{}, input_file:{},"
                    "output_file:{}"
                    .format(debug, diameter, cadence, front_sprocket, log,
                            input_file, output_file))

    # Check the version of Python that is being run against Minimum version
    python_version_check()

    # Call main program, pass values from command line arguments, or variables
    # with their default values which may not have been modified by the cli.
    main(diameter, cadence, front_sprocket, log, input_file, output_file)

"""
Notes:

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 template_l2_19.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 template_l2_19.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/

Cycle Gearing and Cadence info...

https://sporttracks.mobi/blog/practical-building-blocks-gearing
chain rings that are in the 20s and 30s; cyclocross racing – a seeming cross
between a mountain bike and road bike – uses chain rings in the 30s and 40s;
road bikes typically have their rings in the mid to high 30s and low 50s;
time trial and triathlon bikes – built largely for straight and fast speed -
find their chain rings in the high 30s/low 40s and low/mid 50s.

https://en.wikipedia.org/wiki/Crankset
Chainrings vary in size from as few as 20 teeth to as many as 60 and
potentially more.

http://sheldonbrown.com/k7-7.shtml
Cassette
Shimano 7-speed CS-HG70 ac = [28,24,21,18,15,13,11]

https://en.wikipedia.org/wiki/Cadence_(cycling)
Cadence...
Recreational and utility cyclists typically cycle around 60–80 rpm
According to cadence measurement of 7 professional cyclists during 3 week
races they cycle about 90 rpm during flat and long (~190 km) group stages and
individual time trials of ∼50 km. During ∼15 km uphill cycling on high
mountain passes they cycle about 70 rpm.[1]

Wheel diameter information:

24 inch / ISO 507 mm  !609.9mm
The typical 24-inch rim has a diameter of 507 mm (20.0") and an outside
tire diameter of about 24" (about 610 mm).

26 inch / ISO 559 mm
The typical 26-inch rim has a diameter of 559 mm (22.0") and an outside
tire diameter of about 26.2 inches (670 mm).

27.5 inch / ISO 584 mm
use a rim that has a diameter of 584 mm (23.0") with wide, knobby
tires (~27.5 x 2.3 / ISO 58-584)

29 inch / ISO 622 mm
Their rim diameter of 622 mm (~24.5 inch)
The average 29-inch mountain bike tire has an outside diameter of about
28.5 inches (720 mm).
"""

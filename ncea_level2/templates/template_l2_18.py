#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Integer_Fun. template_l2_18.py based on template_master_l2.py
# Introduces: To highlight that python has no limits when performing integer
#       arithmetic. Introduce float data type.
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
_program_ = "Integer_Distance"  # "template_l2_16.py"
_version_ = "1.0"
_date_ = "2016-10-25"
_author_ = "Ian Stewart"
_copyright_ = "© https://creativecommons.org/licenses/by/4.0/"
_description_ = ("Demonstrate the arithmetic performed on integers is \n"
                 "accurate and has no limits.\n"
                 "Introduce floating point calculation.")
_original_ = ("template_master_l2.py - Ian Stewart - October 2016.\n"
              "© https://creativecommons.org/licenses/by/4.0/")

# Global Constants and variables init values. Can be read within functions.
# Can be the default values for arguments of a function.
PYTHON_MIN_VERSION = "3.2"
debug = False
log = "log_{}.txt".format(_program_)
sample = 20
input_file = "./temp/some_data.txt"
output_file = "{}.csv".format(_program_)
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


def main(sample=sample, log=log, in_file=input_file, out_file=output_file):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    message = "Program {} launched.".format(sys.argv[0])
    append_logfile(message, log)

    if debug: print("Program is starting...")

    # Call functions here...
    print("{} is executing...".format(_program_))

    print()
    print("The duration of one Julian year is 365 and 1/4 days")

    print("Seconds in a minute = {}"
          .format(60))

    print("Seconds in one hour = 60 * 60 = {}"
          .format(60 * 60))

    print("Seconds in one day = 60 * 60 * 24 = {}"
          .format(60 * 60 * 24))

    print("Seconds in one quarter of a day = 60 * 60 * 6 = {}"
          .format(60 * 60 * 6))

    # Remains an integer...
    print("Seconds in one Julian year = (60 * 60 * 24 * 365) + (60 * 60 * 6) "
          "= {}"
          .format((60 * 60 * 24 * 365) + (60 * 60 * 6)))

    print()
    print("Distance light travels in 1 second in a vacuum = {} meters"
          .format(299792458))

    print("Distance from Sun to Earth is 1 Astronomical Unit = {} meters"
          .format(149597870700))

    print("Time for light to travel from Sun to Earth = {0} seconds\n"
          "149597870700 // 299792458 = {0}\n"
          .format(149597870700 // 299792458))

    print("Time for light to travel from Sun to Earth = {0}m:{1}s\n"
          "149597870700 // 299792458 // 60 = {0}m\n"
          "149597870700 // 299792458 % 60 = {1}s\n"
          .format(149597870700 // 299792458 // 60,
                  149597870700 // 299792458 % 60))

    print("Distance Light travels in one year = {} meters\n"
          "((60 * 60 * 24 * 365) + (60 * 60 * 6)) * 299792458)"
          .format(((60 * 60 * 24 * 365) + (60 * 60 * 6)) * 299792458))

    print("Distance Light travels in one year (scientific notation) = \n"
          "{:,} meters"
          .format(((60 * 60 * 24 * 365) + (60 * 60 * 6)) * 299792458))

    print()
    distance_light_year = ((60 * 60 * 24 * 365) + (60 * 60 * 6)) * 299792458
    print("Distance to Proxima Centauri (nearest star) =  4.25 light years")

    print("Distance light travels in one quarter of a light year = {} meters"
          .format(distance_light_year // 4))

    print("Distance to Proxima Centauri = {:,} meters"
          .format(distance_light_year * 4 + distance_light_year // 4))
    print()

    # Simlar calculations using floating point...
    input("Type Return to continue")

    print("Seconds in Julian year of 365 1/4 days (as integer) = {}\n"
          "(60 * 60 * 24 * 365) + (60 * 60 * 6)"
          .format((60 * 60 * 24 * 365) + (60 * 60 * 6)))
    print("Type for {}: {}".format((60 * 60 * 24 * 365) + (60 * 60 * 6),
                                   type((60 * 60 * 24 * 365) + (60 * 60 * 6))))

    print("\nCalculations using the floating point data type...")
    print("Seconds in Julian year of 365.25 days (as float) = {}\n"
          "(60 * 60 * 24 * 365.25)"
          .format(60 * 60 * 24 * 365.25))
    print("Type for {}: {}".format(60 * 60 * 24 * 365.25,
                                   type(60 * 60 * 24 * 365.25)))

    print()
    print("Distance light travels in one year = {} meters\n"
          "60 * 60 * 24 * 365.25 * 299792458"
          .format(60 * 60 * 24 * 365.25 * 299792458))
    print()
    print("Distance from Sun to Proxima Centauri = {} meters\n"
          "60 * 60 * 24 * 365.25 * 299792458 * 4.25"
          .format(60 * 60 * 24 * 365.25 * 299792458 * 4.25))

    print("Floating point value changed to base 10 exponential notation.")
    a = (60 * 60 * 24 * 365.25 * 299792458 * 4.25)
    print(a)
    print("Using format(value, '.1f') function, removes the exponential\n"
          "and shows the value to 1 decimal place.")
    print(format(60 * 60 * 24 * 365.25 * 299792458 * 4.25, '.1f'))

    """
    # Demo floats in another template
    print("1234567890123456")
    print(1234567890123456 * 1.0)
    print(float(1234567890123456))
    print(format(1234567890123456 * 1.0, ".1f"))
    print("12345678901234567")
    print(12345678901234567 * 1.0)
    print(float(12345678901234567))
    print(format(12345678901234567 * 1.0, ".1f"))
    print("123456789012345678")
    print(123456789012345678 * 1.0)
    print(float(123456789012345678))
    print(format(123456789012345678 * 1.0, ".1f"))
    print("1234567890123456789")
    print(1234567890123456789 * 1.0)
    print(float(1234567890123456789))
    print(format(1234567890123456789 * 1.0, ".1f"))
    print("12345678901234567890")
    print(12345678901234567890 * 1.0)
    print(float(12345678901234567890))
    print(format(12345678901234567890 * 1.0, ".1f"))
    print("123456789012345678901")
    print(123456789012345678901 * 1.0)
    print(float(123456789012345678901))
    print(format(123456789012345678901 * 1.0, ".1f"))
    """

    append_logfile("Completed Integer_Distance")

    if debug: print("Program is finished.")
    append_logfile("Program {} finished.".format(_program_))
    input("\nPress Enter key to end program.")
    sys.exit()
    # ===== end of main function =====


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
    # print("  -s=, --sample=[VALUE]      Total iterations")
    print("  -h,  --help                Provide this help information.")
    print("  -d,  --debug               Provide additional information \n"
          "                             during program development.")
    # print("  -i=, --input=[FILE]        Input file")
    # print("  -o=, --output=[FILE]       Comma seperated values file")
    print("  -l=, --log=[FILE]          Provide a filename for logging.")
    print("")
    print("Copyright: {}\n".format(_copyright_))


if __name__ == "__main__":
    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):
        if "-h" in option:
            help()
            sys.exit()

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        # -s = total_sample
        if "-s" in option:
            sample_list = sys.argv[index].split("=")
            if len(sample_list) > 1:
                sample = sample_list[1]

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
    if debug: print("Variables: debug:{}, log:{}, input_file:{},"
                    "output_file:{}"
                    .format(debug, log, input_file, output_file))

    # Check the version of Python that is being run against Minimum version
    python_version_check()

    # Call main program, pass values from command line arguments, or variables
    # with their default values which may not have been modified by the cli.
    main(sample, log, input_file, output_file)

"""
Notes:

Explanation on 'Why Python's Integer Division Floors' by  Guido van Rossum
http://python-history.blogspot.co.nz/2010/08/why-pythons-integer-division-floors.html

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 template_l2_18.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 template_l2_18.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/

"""

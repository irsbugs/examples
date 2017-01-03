#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# template_l2_01.py based on template_master_l2.py
# Introduces: Shebang, encoding, Commented text in help(), Importing modules,
#   variables, constants, python2 check, main function, cli help(),
#   if __name__ == "__main__":, cli sys.argv list, debug, call main()
#
# TODO: Describe your program here so that its description will be displayed
# using help(). See pydocs https://docs.python.org/3/library/pydoc.html
# E.g. $ pydoc3 -p 1234 then in a browser http://localhost:1234/

# Template functions utilize modules. Import them now to avoid problems later.
# import modules    # Functions, Strings, Lists used in template:
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
_program_ = "Fundament_Components"  # "template_l2_01.py"
_version_ = "1.0"
_date_ = "2016-10-25"
_author_ = "Ian Stewart"
_copyright_ = "© https://creativecommons.org/licenses/by/4.0/"
_description_ = ("Python program. Fundamental programming style components.\n"
                 "Includes: Shebang, encoding, Commented text in help(), \n"
                 "Importing modules, variables, constants, python2 check, \n"
                 "main function, cli help(), if __name__ == '__main__':, \n"
                 "cli sys.argv list, debug, call main()")

_original_ = ("template_master_l2.py - Ian Stewart - October 2016.\n"
              "© https://creativecommons.org/licenses/by/4.0/")

# Global Constants and variables init values. Can be read within functions.
# Can be the default values for arguments of a function.
PYTHON_MIN_VERSION = "3.2"
debug = False
log = "log_{}.txt".format(_program_)
stuff = 42
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


def main(data=stuff, log=log, in_file=input_file, out_file=output_file):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    if debug: print("Program is starting...")
    if debug: print("data: {}, logfile: {}".format(data, log))
    if debug: print("in_file: {}, out_file: {}".format(in_file, out_file))
    #
    # Call functions here...
    print("Main function is executing. It would normally call other functions")
    print("The program will sleep for 5 seconds")
    # Do nothing for 5 seconds...
    time.sleep(5)

    print("Finished sleeping.")
    if debug: print("Program is finished.")
    input("Press Enter key to end program.")
    sys.exit()
    # ===== end of main function =====

    # Add more functions here...


def help():
    "Provide help on command line options available."
    print("Program: {0}, Version: {1}, Date: {2}, Author: {3}"
          .format(_program_, _version_, _date_, _author_))
    print("{}".format(_description_))
    print("Usage: {} [OPTION]".format(_program_))
    print("Arguments...")
    print("  -h,  --help                Provide this help information.")
    print("  -d,  --debug               Provide additional information \n"
          "                             during program development.")
    print("  -i=, --input=[FILE]        Input file")
    print("  -o=, --output=[FILE]       Output file")
    print("  -s=, --stuff=[VALUE]       Assign a value to stuff")
    print("  -l=, --log=[FILE]          Provide a filename for logging")
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
        # Overide "stuff" global variable.
        # Use = as the delimiter to split keyword and value. E.g.
        # -s=1, --stuff=2, -s="  Has spaces  ", --stuff=Smith, -s=4=four, etc.
        if "-s" in option:
            stuff_list = sys.argv[index].split("=")
            if len(stuff_list) > 1:
                stuff = stuff_list[1]

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
    if debug: print("Variables: debug:{}, stuff:{}, log:{}, input_file:{},"
                    "output_file:{}"
                    .format(debug, stuff, log, input_file, output_file))

    # Call main program, pass values from command line arguments, or variables
    # with their default values which may not have been modified by the cli.
    main(stuff, log, input_file, output_file)

"""
Notes:

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 template_l2_01.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 template_l2_01.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

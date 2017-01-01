#!/usr/bin/env python3
#
import sys

_description_ = """
    Use default integer value or get a string value from the command line.
    Use three methods, type comparison, isinstance() and try/except.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_04_a.py

# Set a default value for variable
stuff = 5


def function_1(value):
    print("Using compare types. Not recommended.")
    print("Function_1 has recieved a value of: {}".format(value))
    print("This value has a type of: {}".format(type(value)))
    # note: PEP 8 Warning: Do not compare types, use 'isinstance()'
    if type(value) == type(1):  # type(1) is <class 'int'>
        print("{} + 25 = {}".format(value, value + 25))
    else:
        print("Not of an integer class. Can not add 25.")
        return


def function_2(value):
    print("Using the isinstance() method")
    print("Function_2 has recieved a value of: {}".format(value))
    print("This value has a type of: {}".format(type(value)))

    if isinstance(value, int):
        print("{} + 35 = {}".format(value, value + 35))
    else:
        print("Not of an integer class. Can not add 35.")
        return


def function_3(value):
    """Use try / except method"""
    print("Using the try / except method.")
    print("Function_3 has recieved a value of: {}".format(value))
    try:
        result = int(value) + 45
        print("{} + 45 = {}".format(value, result))
    except:
        print("Value can not be added to 45")

if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    print("Change the default value with -s=[value] or --stuff=[value]")
    print("E.g. python snip_l2_04.py -s=10")

    for index, option in enumerate(sys.argv):
        # Collect string data from command line interface (cli) sys.argv list
        # Overide "stuff" global variable.
        # Use = as the delimiter to split keyword and value. E.g.
        # -s=1, --stuff=2, etc.
        if "-s" in option:
            stuff_list = sys.argv[index].split("=")
            if len(stuff_list) > 1:
                stuff = stuff_list[1]

    function_1(stuff)
    function_2(stuff)
    function_3(stuff)

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_04_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_04_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

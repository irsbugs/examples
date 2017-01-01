#!/usr/bin/env python3
#
import sys

_description_ = """
    Define a function to get data from the User at the command line.
    Use 'while True' loop to ensure data is entered or data is of the desired
    type.
    Apply format() function to the input() function.
    Use variables to hold text and prompt strings and pass them to the
    function.
    Allow command line options to change prompt and text of input() function
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_05_e.py

# Set variables
text_string = "Input a floating point or integer value"
prompt_string = "3.21"


def get_float_input(text, prompt):
    "Function to get a floating point value."
    while True:
        data = input("\n{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            data = float(data)
            return data
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue

if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    print("Change the prompt value with -p=[value] or --prompt=[value]")
    print("E.g. python snip_l2_05_e.py --prompt=10")
    print("Change the input string with -t=[text] or --text=[text]")
    print("E.g. python snip_l2_05_e.py --text='Radius of circle'")

    for index, option in enumerate(sys.argv):
        # Collect string data from command line interface (cli) sys.argv list
        # Allow overiding "prompt_string" and text_string variables.
        if "-p" in option:
            prompt_list = sys.argv[index].split("=")
            if len(prompt_list) > 1:
                prompt_string = prompt_list[1]

        if "-t" in option:
            text_list = sys.argv[index].split("=")
            if len(text_list) > 1:
                text_string = text_list[1]

    # Call function and pass text and prompt strings.
    value = get_float_input(text_string, prompt_string)
    print("Valid data entered. Value: {}".format(value))

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_05_e.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_05_e.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

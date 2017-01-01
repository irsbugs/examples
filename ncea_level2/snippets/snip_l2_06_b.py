#!/usr/bin/env python3
#
import sys

_description_ = """
    Define a function to get data from the User at the command line.
    Use 'while True' loop to ensure data is entered or data is of the desired
    type. i.e. Integer. If integer is negative return as positive. ie. abs()
    Apply format() function to the input() function.
    Use variables to hold text and prompt strings and pass them to the
    function.
    Allow command line options to change prompt and text of input() function.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_06_b.py

# Set variables
text_string = "Input a +ve or -ve integer"
prompt_string = "5"


def get_positive_integer_entry(text="Input integer value", prompt="0", ):
    """
    Return an absolute abs() integer value from input on the console.
    i.e. If a negative integer is entered it is converted to be positive.
    An integer value as a prompt may be provided. Default prompt string is "0".
    The input prompting text may also be provided.
    """
    while True:
        data = input("{} [{}]:".format(text, prompt))
        if data == "":
            data = prompt
        try:
            data = int(data)
            return abs(data)
        except ValueError as e:
            print("Value Error: {}".format(e))
            print("Please re-enter...")
            continue

if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    print("Change the prompt value with -p=[value] or --prompt=[value]")
    print("E.g. python {} --prompt=10".format(sys.argv[0]))
    print("Change the input string with -t=[text] or --text=[text]")
    print("E.g. python {} --text='People attending meeting'"
          .format(sys.argv[0]))

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
    value = get_positive_integer_entry(text_string, prompt_string)
    print("Valid data entered. Value: {}".format(value))

print("End of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_06_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_06_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

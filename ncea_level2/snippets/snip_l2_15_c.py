#!/usr/bin/env python3
#
import sys
import math
_description_ = """
    Get integer entry as cube edge length. Use functions to calculate cube
    surface area, volume and the lenght of the internal diagonal.
    Use iteration and output data each loop.
    Output the data to a .csv file, suitable for reading into a spreadsheet.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_15_c.py

# Variables
edge_prompt = 1
sample = 20
debug = False
# Define output file variable. E.g. snip_l2_14_b.csv
output_file = "{}.csv".format(sys.argv[0].split(".")[0])


def main(data=edge_prompt, sample=sample, csv_file=output_file):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    if debug: print("Edge: {}, Samples: {}".format(data, sample))
    # Get a integer value for the radius.
    edge = get_integer_entry(data, text="Enter length of cube edge")

    # Get a integer value for the number of samples i.e. range.
    iteration = get_integer_entry(sample, text="Enter number of iterations")

    # Create output file and insert headings
    data = ("{},{},{},{}\n"
            .format("Edge", "Surface", "Volume", "Diagonal"))
    output_to_disk_file(data, csv_file, "write")

    print("\nDimensions of cubes")
    print("{: <15}{: <15}{: <15}{: <15}"
          .format("Edge", "Surface", "Volume", "Diagonal"))
    print("-" * 53)

    for i in range(edge, edge + iteration):

        surface, volume, diagonal = calculate_cube(i)

        print("{: <15g}{: <15g}{: <15g}{: <15g}"
              .format(i, surface, volume, diagonal))

        # Append data to output file.
        data = ("{},{},{},{}\n"
                .format(i, surface, volume, diagonal))
        output_to_disk_file(data, csv_file, "append")

    print("-" * 53)

    print("\nAbove data has been written to the comma separated value file:\n"
          "{}".format(csv_file))


def output_to_disk_file(data, filename, action=None):
    if action is None:
        return
    if action == "append":
        f = open(filename, "a")
        f.write(data)
    if action == "write":
        f = open(filename, "w")
        f.write(data)
    f.close()


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
            return abs(int(data))
        except ValueError as e:
            if debug: print("Value Error: {}".format(e))
            continue


def calculate_cube(edge):
    "Calculate cube surface area, volume, internal diagonal"
    surface = 6 * edge ** 2
    volume = edge ** 3
    diagonal = math.sqrt(3) * edge
    return surface, volume, diagonal


if __name__ == "__main__":
    print("Program {} has started...".format(sys.argv[0]))
    print("Enable debugging with -d or --debug")
    print("E.g. python {} --debug".format(sys.argv[0]))
    print("Set edge prompt value -e= or --edge=")
    print("E.g. python {} --edge=5".format(sys.argv[0]))
    print("Set number of samples -s= or --samples=")
    print("E.g. python {} --samples=20".format(sys.argv[0]))
    print("Set CSV filename -o= or --output=")
    print("E.g. python {} --output=circle_data.csv".format(sys.argv[0]))
    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        if "-e" in option:
            edge_prompt_list = sys.argv[index].split("=")
            if len(edge_prompt_list) > 1:
                edge_prompt = edge_prompt_list[1]

        if "-s" in option:
            sample_list = sys.argv[index].split("=")
            if len(sample_list) > 1:
                sample = sample_list[1]

        if "-o" in option:
            output_file_list = sys.argv[index].split("=")
            if len(output_file_list) > 1:
                output_file = output_file_list[1]
    main(edge_prompt, sample, output_file)

print("\nEnd of program.")
input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_15_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_15_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

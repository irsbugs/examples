#!/usr/bin/env python3
#
import sys
import math
_description_ = """
    Get integer entry as cube edge length. Calculate cube surface area, volume
    and the lenght of the internal diagonal. Use iteration and output data
    each loop.
    Output the data to a .csv file, suitable for reading into a spreadsheet
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_15_a.py

# Variables. Define output file variable. E.g. snip_l2_14_a.csv
csv_file = "{}.csv".format(sys.argv[0].split(".")[0])

print("Program {} has started...".format(sys.argv[0]))

edge = input("Enter integer value of edge length of cube: ")
try:
    edge = abs(int(edge))
except:
    print("Invalid edge. Exiting...")
    sys.exit()

iteration = input("Enter integer value for number of iterations: ")
try:
    iteration = abs(int(iteration))
except:
    print("Invalid number for iteration. Exiting...")
    sys.exit()

# Create output file and insert headings
f = open(csv_file, "w")
f.write("{},{},{},{}\n"
        .format("Edge", "Surface", "Volume", "Diagonal"))
f.close()

# Display headings on console terminal
print("\nDimensions of cubes")
print("{: <15}{: <15}{: <15}{: <15}"
      .format("Edge", "Surface", "Volume", "Diagonal"))
print("-" * 53)
for i in range(edge, edge + iteration):
    surface = 6 * i ** 2
    volume = i ** 3
    diagonal = math.sqrt(3) * i
    print("{: <15g}{: <15g}{: <15g}{: <15g}"
          .format(i, surface, volume, diagonal))

    # Append data to output file.
    f = open(csv_file, "a")
    f.write("{:g},{:g},{:g},{:g}\n"
            .format(i, surface, volume, diagonal))
    f.close()

print("-" * 53)

print("\nAbove data has been written to the comma separated value file:\n"
      "{}".format(csv_file))
print("\nEnd of program.")

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_15_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_15_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

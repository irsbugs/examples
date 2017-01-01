#!/usr/bin/env python3
#
import sys

_description_ = """
    Real scenario demonstration of large integers and integer operators.
    Addition +, Multiplicaton *, Integer Division //, Modulo %
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_18_a.py

print()
print("Large integer mathematics.")
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

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_18_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_18_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

#!/usr/bin/env python3
#
import sys
import math

_description_ = """
    Bicycle pedding cadence and sprocket ratios to determine speeds in each
    gear. Introduces list[] and for loop iterating over a list.
    Simple programming flow style.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_19_a.py

# Wheel diameter of ~ 0.318309m has 1 meter circumference. 1/pi
diameter_prompt = 0.67  # 1/math.pi
WHEEL_MIN = 0.3
WHEEL_MAX = 0.75

# Cadence: 60 to 80 normal riding. Racing: 70 up hills and 90 the flat.
cadence_prompt = 60
CADENCE_MIN = 40
CADENCE_MAX = 120

front_sprocket_prompt = 50  # Crankset_teeth. Range 20 to 60 teeth.
FRONT_SPROCKET_MIN = 20
FRONT_SPROCKET_MAX = 60

rear_sprocket_list = [28, 24, 21, 18, 15, 13, 11]  # Shimano 7-speed CS-HG70 ac

# Get diameter and if value is outside of min or max force value into range
diameter = input("Enter wheel diameter. Range {} to {} meters. [{}] :"
                 .format(WHEEL_MIN, WHEEL_MAX, diameter_prompt))

if diameter == "":
    diameter = diameter_prompt

try:
    diameter = float(diameter)
except:
    print("Diameter is not a floating point value. Exiting...")
    sys.exit()

if diameter < WHEEL_MIN:
    diameter = WHEEL_MIN
if diameter > WHEEL_MAX:
    diameter = WHEEL_MAX

print("Diameter of wheel in meters: {}".format(diameter))

# Get cadence and if value is outside of min or max force value into range
cadence = input("Enter Pedalling cadence (Revolutions per minute) [{}]: "
                .format(cadence_prompt))

if cadence == "":
    cadence = cadence_prompt

try:
    cadence = int(cadence)
except:
    print("Invalid cadence of {}. Exiting...".format(cadence))
    sys.exit()

if cadence < CADENCE_MIN:
    cadence = CADENCE_MIN
if cadence > CADENCE_MAX:
    cadence = CADENCE_MAX
print("Pedalling Cadence: {}".format(cadence))

# Get sprocket and if value is outside of min or max force value into range
front_sprocket = input("Teeth on front sprocket [{}]: "
                       .format(front_sprocket_prompt))
if front_sprocket == "":
    front_sprocket = front_sprocket_prompt
try:
    front_sprocket = int(front_sprocket)
except:
    print("Invalid front sprocket of {}. Exiting...".format(front_sprocket))

if front_sprocket < FRONT_SPROCKET_MIN:
    front_sprocket = FRONT_SPROCKET_MIN
if front_sprocket > FRONT_SPROCKET_MAX:
    front_sprocket = FRONT_SPROCKET_MAX
print("Teeth on front sprocket: {}".format(front_sprocket))

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

input("Press Enter key to end program")
sys.exit()
"""
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_19_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_19_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

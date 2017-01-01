#!/usr/bin/env python3
import sys
import time
import platform

_description_ = """
    Demonstrate ANSI escape sequences for direct cursor addressing and setting
    forground and back ground colours on a console.
    Perform line drawing on a console using the box drawing character set.
    On Microsoft Windows console this is better than using the ANSI escape
    sequence box drawing as it is missing the ability to do the cross-hairs.
    Draw vertical bars of colour and indicates their numeric colour value.
    A draw_rectangle function has the arguments (x, y, width,height, foreground
    colour, background colour).
    Also sets the console windows title with ESC ] 2 ; <string> BEL
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_23_b.py

# Initialise constants
ESC = chr(27)  # Escape character
CSI = ESC + "["  # Control Sequence Introducer
BEL = chr(7)
# Set if you want to pause between screens and hit return to continue
pause = True
delay = True
delay_duration = 0.4
foreground = (30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97)
background = (40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105,
              106, 107)

# Enable Win10 CMD window to support ANSI esacpe sequences.
if platform.system() == "Windows":
    print("\nMicrosoft {} Release: {} Version: {}"
          .format(platform.system(), platform.release(), platform.version()))
    ver_list = platform.version().split(".")
    if int(platform.release()) < 10:
        print("Requires Windows version 10 or higher for ANSI support.")
        print("Exiting...")
        sys.exit()

    if len(ver_list) >= 2:  # E.g. ['10', '0', '14393']
        # print(ver_list)
        minor_version = float((ver_list[1] + "." + ver_list[2]))
        # print(minor_version)  # E.g. 0.14393

        if minor_version >= 0.10586:
            print("Version of Win10 should support ANSI escape sequences.")
        else:
            print("Win10 requires updating to support ANSI escape sequences.")
            print("Minimum version: 10.0.10586 'Threshold 2' 10 May 2016.")
            print("Exiting...")
            sys.exit()
            # 10.0.14393 is "The Anniversary Update". Released 2 Aug 2016.
    if int(platform.release()) >= 10:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        status = kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        if status == 0:
            print("Error returned attempting to set ANSI escape sequences.")
        else:
            print("Windows CMD window has been set for ANSI escape sequences.")
            print()
            t = ("For more information on Microsoft use of ANSI escape codes"
                 "\nplease visit this web-page...\n"
                 "https://msdn.microsoft.com/en-us/library/mt638032(v=vs.85)"
                 ".aspx")
            print(t)
    if delay: time.sleep(2)
    if pause: input("\nType Return key to continue")


def draw_rectangle(start_column=1, start_row=1, width=80, height=23,
                   foreground_colour=39, background_colour=49):
    """
    Draw a rectangle using characters from Box Drawing character set.
    0x2500 to 0x257f
    Single top and single side from box drawing characgter set.
     ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

    # start_column = 1  # Columns start count at 1
    # start_row = 1  # Rows start count at 1
    # width = 80  # Min. width = 2 Max greater than 80 columns then drop chars
    # height = 24  # Min. height = 2 Max of 24 or 25. But could be more.
    """
    # Set foreground and background colours
    print("{}{}m{}{}m".format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)

    # Top line
    # Prints horizontal line. E.g. From position 2 to column 79
    # Adds corners. E.g. At positions 1 and 80.
    for i in range(start_column + 1, start_column + width - 1):
        print("{}{};{}H─".format(CSI, start_row, i),
              end="", flush=True)
    print("{}{};{}H┌".format(CSI, start_row, start_column),
          end="", flush=True)
    print("{}{};{}H┐".format(CSI, start_row, start_column + width - 1),
          end="", flush=True)

    # Middle lines
    # Adds the vertical lines on each side of the rectangle. Positions 1 and 80
    for j in range(start_row + 1, start_row + height - 1):
        print("{}{};{}H│".format(CSI, j, start_column),
              end="", flush=True)
        print("{}{};{}H│".format(CSI, j, start_column + width - 1),
              end="", flush=True)

    # Bottom line
    # Prints horizontal line. E.g. From position 2 to column 79
    # Adds bottom corners. E.g. At positions 1 and 80.
    for i in range(start_column + 1, start_column + width - 1):
        print("{}{};{}H─".format(CSI, start_row + height - 1, i),
              end="", flush=True)
    print("{}{};{}H└".format(CSI, start_row + height - 1, start_column),
          end="", flush=True)
    print("{}{};{}H┘"
          .format(CSI, start_row + height - 1, start_column + width - 1),
          end="", flush=True)

    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


# Program starts here...
# Clear screen
print("{}2J".format(CSI), end="", flush=True)

# Set the Console window title bar...
# Note right square bracket - not left bracket - ESC ] 2 ; <string> BEL
text = "Colour Bars and their foreground and background numbers"
print("{}]2;{}{}".format(ESC, text, BEL), end="", flush=True)
print(BEL)
if delay: time.sleep(1)

# Display all 16 colours as bars. Each colour is 4 char positions wide.
# Draw as a two rectangles. A rectangle with a smaller rectangle inside.
# Numeric values for foreground and background colours. CSI<colour value>m

# Draw pairs of rectangles of each colour using a for loop
for i in range(16):
    x = i * 4 + 1
    y = 1
    width = 4
    height = 18
    f_colour = foreground[i]
    b_colour = background[i]
    draw_rectangle(x, y, width, height, f_colour, b_colour)
    draw_rectangle(x + 1, y + 1, width - 2, height - 2, f_colour, b_colour)
    if delay: time.sleep(delay_duration)

# Add information at bottom of screen. Lines 21 through 25...
for index, value in enumerate(foreground):
    print("{}{};{}H{}".format(CSI, 19, index * 4 + 2, value),
          end="", flush=True)
print("{}{};{}H<--Foreground".format(CSI, 19, 65), end="", flush=True)

for index, value in enumerate(background):
    print("{}{};{}H{}".format(CSI, 20, index * 4 + 2, value),
          end="", flush=True)
print("{}{};{}H<--Background".format(CSI, 20, 65), end="", flush=True)

text = "Colours are selected with Escape [ <n> m also referred to as CSI<n>m"
print("{}{};{}H{}"
      .format(CSI, 22, 1, text), end="", flush=True)
text = "Where <n> is a foreground or background value from above."
print("{}{};{}H{}"
      .format(CSI, 23, 1, text), end="", flush=True)
if pause: input("{}(B{}{};{}HType Return key to continue"
                .format(ESC, CSI, 24, 1))


print("{}2J".format(CSI))  # Clear screen
# Same drawing as above but colours in opposite order.
# No for loop. Code for each call to draw_rectangle()
# draw_rectangle(x, y, width, height, f_colour, b_colour)
# Brighter colour pairs of rectangles...
draw_rectangle(1, 1, 4, 18, 97, 107)
draw_rectangle(2, 2, 2, 16, 97, 107)

draw_rectangle(5, 1, 4, 18, 96, 106)
draw_rectangle(6, 2, 2, 16, 96, 106)

draw_rectangle(9, 1, 4, 18, 95, 105)
draw_rectangle(10, 2, 2, 16, 95, 105)

draw_rectangle(13, 1, 4, 18, 94, 104)
draw_rectangle(14, 2, 2, 16, 94, 104)

draw_rectangle(17, 1, 4, 18, 93, 103)
draw_rectangle(18, 2, 2, 16, 93, 103)

draw_rectangle(21, 1, 4, 18, 92, 102)
draw_rectangle(22, 2, 2, 16, 92, 102)

draw_rectangle(25, 1, 4, 18, 91, 101)
draw_rectangle(26, 2, 2, 16, 91, 101)

draw_rectangle(29, 1, 4, 18, 90, 100)
draw_rectangle(30, 2, 2, 16, 90, 100)

# Normal colours...
draw_rectangle(33, 1, 4, 18, 37, 47)
draw_rectangle(34, 2, 2, 16, 37, 47)

draw_rectangle(37, 1, 4, 18, 36, 46)
draw_rectangle(38, 2, 2, 16, 36, 46)

draw_rectangle(41, 1, 4, 18, 35, 45)
draw_rectangle(42, 2, 2, 16, 35, 45)

draw_rectangle(45, 1, 4, 18, 34, 44)
draw_rectangle(46, 2, 2, 16, 34, 44)

draw_rectangle(49, 1, 4, 18, 33, 43)
draw_rectangle(50, 2, 2, 16, 33, 43)

draw_rectangle(53, 1, 4, 18, 32, 42)
draw_rectangle(54, 2, 2, 16, 32, 42)

draw_rectangle(57, 1, 4, 18, 31, 41)
draw_rectangle(58, 2, 2, 16, 31, 41)

draw_rectangle(61, 1, 4, 18, 30, 40)
draw_rectangle(62, 2, 2, 16, 30, 40)

# Add information at bottom of screen. Lines 20 through 24...
# print("{}{}M".format(CSI,20)) # Delete line
# print("{}{}M".format(CSI,21)) # Delete line
for index, value in enumerate(reversed(foreground)):
    print("{}{};{}H{}".format(CSI, 19, index * 4 + 2, value),
          end="", flush=True)
print("{}{};{}H<--Foreground".format(CSI, 19, 65), end="", flush=True)

for index, value in enumerate(reversed(background)):
    print("{}{};{}H{}".format(CSI, 20, index * 4 + 2, value),
          end="", flush=True)
print("{}{};{}H<--Background".format(CSI, 20, 65), end="", flush=True)

text = "Colours are selected with Escape [ <n> m also referred to as CSI<n>m"
print("{}{};{}H{}"
      .format(CSI, 22, 1, text), end="", flush=True)
text = "Where <n> is a foreground or background value from above."
print("{}{};{}H{}"
      .format(CSI, 23, 1, text), end="", flush=True)
if pause: input("{}(B{}{};{}HType Return key to end program"
                .format(ESC, CSI, 24, 1))

input("Press Enter key to end program")
sys.exit()

"""
Notes / Links:

http://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console

http://www.nivot.org/blog/post/2016/02/04/Windows-10-TH2-%28v1511%29-Console-Host-Enhancements

Draw a rectangle using characters from Box Drawing character set.
0x2500 to 0x257f. Single top and single side from box drawing characgter set.
 ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

ANSI escape codes invoked by microsoft...
https://msdn.microsoft.com/en-us/library/mt638032(v=vs.85).aspx

Support for Direct Cursor addressing CSI y ; x H
text = "Hello"
print("{}{};{}H{}".format(CSI, 22, 1, text), end="", flush=True)

Support for Line drawing...
print(ESC + "(0") # Enter line drawing

Line drawing that fails under Win10...
print('n') <-- should produce a crossing of lines

Undocumented Win10 output in Line drawing mode...
print("|")  # <-- π
print("}")  # <-- £
print("|")  # <-- ≠
print("a")  # <-- Hash block
print("f")  # <-- degrees symbol
print("y")  # <-- ≤
print("z")  # <-- ≥
print("g")  # <-- plus or minus symbol

Exit line drawing - Return to Ascii
print(ESC + "(B") # Ascii character mode

Note: Better to use characters from the Box Drawing set 0x2500 to 0x257f.

===
Colours
Background
16 colours - Background
49 = Background default
48 = Background Extended - Does not provide and more colours

40 = Black

41 = Dark Red
42 = Dark Green
43 = Dark Yellow
44 = Dark Blue
45 = Dark Magenta
46 = Dark Cyan

47 = Light Grey
100 = Dark Grey

101 = Bright Red
102 = Bright Green
103 = Bright Yellow
104 = Bright Blue
105 = Bright Magenta
106 = Bright Cyan

107 = White

===

Foreground
16 colours - Foreground
38 Foreground extended
39 Foreground default

30 = Black

31 = Dark Red
32 = Dark Green
33 = Dark Yellow
34 = Dark Blue
35 = Dark Magenta
36 = Dark Cyan

37 = Light Grey
90 = Dark Grey

91 = Bright Red
92 = Bright Green
93 = Bright Yellow
94 = Bright Blue
95 = Bright Magenta
96 = Bright Cyan

97 = White
To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_23_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_23_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

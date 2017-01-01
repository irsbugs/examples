#!/usr/bin/env python3

import sys
import time
import platform

_description_ = """
    Demostrate ANSI escape sequences on a console. Including Microsoft Win10.
    By default, most Linux consoles support the ANSI escape sequences.
    Windows 10, since May 2016, supports a subset of ANSI escape sequences,
    for the CMD and Powershell console windows. On Windows this functionality
    is turned off by default.
    Enabling the ANSI escape sequences in Win10 can be performed by python:
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    See notes section for links on ANSI escape sequences.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_23_a.py

# Initialise constants
ESC = chr(27)  # Escape character
CSI = ESC + "["  # Control Sequence Introducer
# Set pause if you want to pause between screens and hit return to continue
pause = True
delay = True
verbose = True

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
        #print(ver_list)
        minor_version = float((ver_list[1] + "." + ver_list[2]))
        #print(minor_version)  # E.g. 0.14393
        
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

# Erase display. i.e. Replace with spaces
print(CSI + "2J", end="", flush=True)

# Set console column with to 80 columns
print(CSI + "?3l", end="", flush=True)  # 80 col
# print(CSI + "?3h", end="", flush=True)  # 132 col

# Set dark green background with white foreground and eraze the display
print(CSI + "42m")  # set background colour 41 red 42 green
print(CSI + "97m")  # set forground white

# Eraze display. Three methods of erazing the display...
print(CSI + "2J")
print(CSI + "2J", end="", flush=True)
print("{}2J".format(CSI), end="", flush=True)

# Positioning the screen starts at co-ordinates 1,1
# CSI + Line-down-the-screen (y axis) ; Character-cell-in-line (x axis) + H
# print(CSI + "1;1H" + "o <--Postion:1;1")
for i in range(1, 22):
    print("{}{};{}Ho <--Position:{},{}".format(CSI, i, i, i, i),
          end="", flush=True)

if delay: time.sleep(2)

# Positioning on the screen at 1:3 angle
for i in range(1, 22):
    print("{}{};{}Ho <--Position:{},{}".format(CSI, i, i * 3, i, i * 3),
          end="", flush=True)

print("{}{};{}HThe above is direct cursor addressing. CSI y-axis ; x-axis H"
      .format(CSI, 22, 1), end="", flush=True)
print("{}{};{}HSetting to 132 column screen".format(CSI, 23, 1),
      end="", flush=True)
if delay: time.sleep(2)
if pause: input("{}{};{}HType Return key to continue".format(CSI, 24, 1))

# Change to 132 column
# print(CSI + "?3h")  # 132 col
print("{}?3h".format(CSI), end="", flush=True)

# Positioning on the screen at 1:3 angle
for i in range(1, 22):
    print("{}{};{}Ho <--Position:{},{}".format(CSI, i, i * 4, i, i * 4))

text = "Screen as 132 column, but cursor addressing may limit at column 80"
print("{}{};{}H{}".format(CSI, 22, 1, text),
      end="", flush=True)

# Erase previous contents of line 23
# print("{}{}M".format(CSI, 23), end="", flush=True)

print("{}{};{}HRe-setting to 80 column screen".format(CSI, 23, 1),
      end="", flush=True)
if delay: time.sleep(2)
if pause: input("{}{};{}HType Return key to continue to colour demonstrations"
                .format(CSI, 24, 1))
print("{}?3l".format(CSI), end="", flush=True)  # 80 col


# Normal Background/foreground and Bright background/foreground Colours
normal_colour = ("black", "red", "green", "yellow", "blue", "magenta",
                 "cyan", "light grey")

bright_colour = ("dark grey", "bright red", "bright green", "bright yellow",
                 "bright blue", "bright magenta", "bright cyan", "white")

# Backgrounds.
for i in range(8):
    # Normal Background: 40 to 47. black + 6 x colours + light grey
    print("{}{}m".format(CSI, 97))  # CSI + foreground colour + m - 97 = white
    print("{}{}m".format(CSI, 40 + i))  # CSI + background colour + m
    print("{}2J".format(CSI))  # Eraze display.
    print("{}{};{}HNormal Background colour value (40 to 47): {} - {}"
          .format(CSI, 2, 2, 40 + i, normal_colour[i]), end="", flush=True)
    if delay: time.sleep(0.5)

for i in range(8):
    # Bright Background: 100 to 107. dark grey + 6 x bright colours + white
    print("{}{}m".format(CSI, 30))  # CSI + foreground colour + m - 97 = black
    print("{}{}m".format(CSI, 100 + i))  # CSI + background colour + m
    print("{}2J".format(CSI))  # Erase display.
    print("{}{};{}HBright Background colour value (100 to 107): {} - {}"
          .format(CSI, 2, 2, 100 + i, bright_colour[i]), end="", flush=True)
    if delay: time.sleep(0.5)

# Foregrounds
for i in range(8):
    # Normal Forground: 30 to 37. black + 6 x colours + light grey
    print("{}{}m".format(CSI, 30 + i))  # CSI + foreground colour + m
    print("{}{}m".format(CSI, 107))  # CSI + background colour + m 107 = white
    print("{}2J".format(CSI))  # Erase display.
    print("{}{};{}HNormal Foreground colour value (30 to 37): {} - {}"
          .format(CSI, 2, 2, 30 + i, normal_colour[i]), end="", flush=True)
    if delay: time.sleep(0.5)

# Foregrounds
for i in range(8):
    # Bright Forground: 90 to 97. dark grey + 6 x bright colours + white
    print("{}{}m".format(CSI, 47))  # CSI + background colour + m - 47 = l grey
    print("{}{}m".format(CSI, 90 + i))  # CSI + foreground colour + m
    print("{}2J".format(CSI))  # Erase display.
    print("{}{};{}HBright Foreground colour value (90 to 97): {} - {}"
          .format(CSI, 2, 2, 90 + i, bright_colour[i]), end="", flush=True)
    if delay: time.sleep(0.5)

# Although colours can be extended CSI38m (foreground) CSI48 (background) to
# accept RGB colour values, these get reduced to the totla of 16 colours.

text = "Type Return key to continue to text formatting"
if pause: input("{}{};{}H{}".format(CSI, 24, 1, text))


# Underline, negative, bolding. sequences
print("{}{}m".format(CSI, 32))  # Normal green foreground
print("{}{}m".format(CSI, 107))  # CSI + background colour + m 107 = white
print("{}2J".format(CSI))  # Erase display.
# Set a default
print("{}{};{}HNormal green foreground CSI32m with white background CSI107m"
      .format(CSI, 2, 2), end="", flush=True)

# Bold/Bright - Brightens
print("{}{}HNot demonstrated. Brightening text with CSI1m. Does not restore."
      .format(CSI, 4, 2), end="", flush=True)

# Switch underline on
print("{}{}m".format(CSI, 4))
print("{}{};{}HUnderline has been turned on. CSI4m"
      .format(CSI, 6, 2), end="", flush=True)
# Switch underline off
print("{}{}m".format(CSI, 24))
print("{}{};{}HUnderline has been turned off. CSI24m"
      .format(CSI, 8, 2), end="", flush=True)

# Switch foreground / backgound.
print("{}{}m".format(CSI, 7))
print("{}{};{}HThe background and foreground have been switched. CSI7m"
      .format(CSI, 10, 2), end="", flush=True)
# Restore foreground / backgound.
print("{}{}m".format(CSI, 27))
print("{}{};{}HThe background and foreground have been restored. CSI27m"
      .format(CSI, 12, 2), end="", flush=True)

if delay: time.sleep(2)

# Reset background to default - 49
print("{}{}m".format(CSI, 49))
print("{}{};{}HBackground reset to its default colour. CSI49m"
      .format(CSI, 14, 2), end="", flush=True)
if delay: time.sleep(2)

print("{}{}m".format(CSI, 39))
print("{}{};{}HForeground reset to its default colour. CSI39m"
      .format(CSI, 16, 2), end="", flush=True)

# Restore to default values
print("{}{}".format(CSI, 0))
print("{}{};{}HReset all attributes to default values. CSI0m."
      .format(CSI, 18, 2), end="", flush=True)

if delay: time.sleep(2)
text = "Type Return key to continue to line drawing mode"
if pause: input("{}{};{}H{}".format(CSI, 24, 1, text))

# Erase display. i.e. Replace with spaces
print(CSI + "2J", end="", flush=True)

# Drawing Mode
# DEC Line Drawing set...
print(ESC + "(B")  # Ascii mode
print("{}{}HTurn on Line Drawing Mode. ESC(0"
      .format(CSI, 2, 2))
print("With Line Drawing on then the following characters produce the lines")
print("j k l m n q t u v w x" + ESC + "(0")  # Enter line drawing
print("j k l m n q t u v w x", end="", flush=True)
print(ESC + "(B", end="", flush=True)  # Ascii mode
print("\nNote that 'n' should produce a cross of lines. A square is an error.")
print()

# Normal characters under Drawing mode
print("In line drawing mode the following upper case characters and symbols\n"
      "are available.")
print(ESC + "(0")  # Enter line drawing
print(" A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ")
print(" . , ; : ' [ ] _ - + = ! @ # $ % ^ & * ( ) < > ? / ")
print(" 0 1 2 3 4 5 6 7 8 9 ")
print(ESC + "(B")  # Ascii mode
print()

# Extra characters under Drawing mode
print("Some ascii characters produce different symbols in line drawing")
print(" a f g y z ~ { } | " + ESC + "(0")  # plus enter line drawing
print(" a f g y z ~ { } | ", end="", flush=True)
print(ESC + "(B")  # Ascii mode
# a = Hash block, f = degrees, g = plus/minus, y = less than equals,
# z = greater than equals, ~ = dot , { = pi, } = pound, | = not equal
if pause: input("{}{};{}HType Return key to continue".format(CSI, 24, 1))

# Erase display. i.e. Replace with spaces
print(CSI + "2J", end="", flush=True)
print("{}{};{}H".format(CSI, 1, 1))

# Characters that return a square
print("Some ascii characters result in square symbol on Windows")
print("On linux they are FF, VT, 1st Hor line, cross-hairs, 3 x Hor lines")
print(" c i o n p r s " + ESC + "(0")  # plus enter line drawing
print(" c i o n p r s ", end="", flush=True)  # squares
print(ESC + "(B")  # Ascii mode

# Characters that return a square
print("Some ascii characters that have no character output on Windows")
print("b = HT, d = CR, e = LF, h = NL")
print(" b d e h " + ESC + "(0")  # plus enter line drawing
print(" b d e h ", end="", flush=True)  # squares
print(ESC + "(B")  # Ascii mode
if delay: time.sleep(2)

text = "Type Return key to continue to line drawing examples"
if pause: input("{}{};{}H{}".format(CSI, 24, 1, text))
# Erase display. i.e. Replace with spaces
print(CSI + "2J", end="", flush=True)

print("{}{};{}HLine Drawing\n{}(0"
      .format(CSI, 2, 2, ESC,), end="", flush=True)

# n produces a square on Windows, should be a cross-hair graphic.
# Each print function includes a newline character (\n).
print(" lqqqwqqqk")
print(" x   x   x")
print(" x 0 x 1 x")
print(" x   x   x")
print(" tqqqnqqqu")
print(" x   x   x")
print(" x 2 x 3 x")
print(" x   x   x")
print(" mqqqvqqqj")

# n produces a square on Windows, should be a cross-hair graphic.
print(" lqqqqqqqqqqqqqqqqqqqqqqqqqqqqwqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqk")
print(" x                            x                                 x")
print(" x           HELLO            x                WORLD            x")
print(" x                            x                                 x")
print(" x                            x                                 x")
print(" tqqqqqqqqqqqqqqqqqqqqqqqqqqqqnqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqu")
print(" x                            x                                 x")
print(" x                            x                                 x")
print(" mqqqqqqqqqqqqqqqqqqqqqqqqqqqqvqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqj")
print(ESC + "(B")  # Ascii character mode

print("{}{};{}HLine Drawing off. Returned to Ascii character mode."
      .format(CSI, 22, 2), end="", flush=True)
print("{}{};{}HEnd of Escape sequence presentation..."
      .format(CSI, 23, 2), end="", flush=True)
if delay: time.sleep(2)
if pause: input("{}{};{}HType Return key to end program".format(CSI, 24, 1))

# Restore the default background colour
print(CSI + "49" + "m")
# print("Restore default background colour value: 49")

# Restore the default foreground colour
print(CSI + "39" + "m")
# print("Restore default foreground colour value: 39")

# Erase display.
print(CSI + "2J", end="", flush=True)
input("Press Enter key to end program")
sys.exit()

"""
Notes / Links:

http://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console

http://www.nivot.org/blog/post/2016/02/04/Windows-10-TH2-%28v1511%29-Console-Host-Enhancements

ANSI escape codes invoked by microsoft...
https://msdn.microsoft.com/en-us/library/mt638032(v=vs.85).aspx

Enter Line drawing...
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
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_23_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_23_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

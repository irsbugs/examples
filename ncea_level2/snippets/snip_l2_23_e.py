#!/usr/bin/env python3
import sys
import time
import platform
import ctypes

_description_ = """
    Demonstrate ANSI escape sequences for direct cursor addressing and setting
    forground and back ground colours on a console.
    Perform line drawing on a console using the box drawing character set.
    On Microsoft Windows console this is better than using the ANSI escape
    sequence box drawing as it is missing the ability to do the cross-hairs.
    Introduce write_field() function.
    Proceedural functions: main()
    Called functions()
    escape_sequence_check() - To check if Win10 is at the correct version
    draw_rectangle()
    draw_horizontal_line()
    draw_vertical_line()
    draw_intersection_line()
    colour_check() - Check if colour value is valid or translate text of
                     colour to numeric value.
    write_text() - Direct cursor addressing of text strings
    write_field() - Includes length and alignment of text in the field
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_23_e.py

# Initialise constants
ESC = chr(27)  # Escape character
CSI = ESC + "["  # Control Sequence Introducer
BEL = chr(7)

# Set if you want to pause between screens and hit return to continue
pause = True
delay = True
delay_duration = 0.4
debug = True
# Create a colour dictionary to translate colours to numeric values
# Dictionary values are (foreground colours, background colours).
COLOUR = {"black": (30, 40),  # 16 colours available
          "red": (31, 41),
          "green": (32, 42),
          "yellow": (33, 43),
          "blue": (34, 44),
          "magenta": (35, 45),
          "cyan": (36, 46),
          "light_grey": (37, 47),
          "grey": (90, 100),
          "light_red": (91, 101),
          "light_green": (92, 102),
          "light_yellow": (93, 103),
          "light_blue": (94, 104),
          "light_magenta": (95, 105),
          "light_cyan": (96, 106),
          "white": (97, 107),
          "dark_red": (31, 41),  # Allow dark prefix for 7 x normal colours
          "dark_green": (32, 42),
          "dark_yellow": (33, 43),
          "dark_blue": (34, 44),
          "dark_magenta": (35, 45),
          "dark_cyan": (36, 46),
          "dark_grey": (90, 100),
          "bright_grey": (37, 47),  # Allow bright prefix for 7 x light colours
          "bright_red": (91, 101),
          "bright_green": (92, 102),
          "bright_yellow": (93, 103),
          "bright_blue": (94, 104),
          "bright_magenta": (95, 105),
          "bright_cyan": (96, 106),
          "default": (39, 49)  # Allow name "default" for the default colours
          }


def main():
    "Demonstrate the write_field() method."
    # write_text(text="", start_column=1, start_row=1, foreground_colour=39,
    #           background_colour=49)
    # write_field(text="", start_column=1, start_row=1, length=20,
    #            align="left", foreground_colour=39, background_colour=49)
    # Check if it Windows 10 at correct version and turn on Escape sequences
    escape_sequence_check()
    print("{}2J".format(CSI))  # Clear screen

    text = "Demonstation of write_field() function..."
    write_field(text, 1, 1, 40, "left")

    text = "Hello - left length 40"
    write_field(text, 6, 2, 40, "left", "light_cyan", "dark_green")

    text = "Hello - centre length 40"
    write_field(text, 6, 3, 40, "centre", "light_yellow", "dark_blue")

    text = "Hello - right length 40"
    write_field(text, 6, 4, 40, "right",)  # "light_blue", "light_grey")
    if pause: input("{}{};{}Htype return to continue".format(CSI, 10, 1))

    # Draw a rectangle and demonstrate allignment of text in the rectangle
    # plus the clearing of previous text in the field.
    # draw_rectangle(x, y, width, height, f_colour, b_colour)
    draw_rectangle(5, 5, 42, 3, "light_blue", "red")

    text = "Hello - left length 40"
    write_field(text, 6, 6, 40, "left", "light_cyan", "dark_green")
    if pause: input("{}{};{}Htype return to continue".format(CSI, 10, 1))

    text = "Hello - centre length 40"
    write_field(text, 6, 6, 40, "centre", "light_yellow", "dark_blue")
    if pause: input("{}{};{}Htype return to continue".format(CSI, 10, 1))

    text = "Hello - right length 40"
    write_field(text, 6, 6, 40, "right",)  # "light_blue", "light_grey")
    if pause: input("{}{};{}Htype return to continue".format(CSI, 10, 1))
    input("Press Enter key to end program")
    sys.exit()


def escape_sequence_check():
    """
    Check the platform. If windows 10, then enable Terminal Escape sequences.
    Requires: platform and ctypes modules
    Reads: if debug, if delay, and if pause global variables
    """
    if platform.system() == "Windows":
        if debug: print("Microsoft {} Release: {} Version: {}"
                        .format(platform.system(), platform.release(),
                                platform.version()))
        ver_list = platform.version().split(".")
        if int(platform.release()) < 10:
            print("Requires Windows version 10 or higher for ANSI support.")
            print("Exiting...")
            sys.exit()
        if len(ver_list) >= 2:
            if int(ver_list[2]) >= 10586:
                s = "This version of Win10 supports ANSI escape sequences."
                if debug: print(s)
            else:
                s = ("Win10 requires updating to support ANSI escape "
                     "sequences.\nMinimum version: 10.0.10586 'Threshold 2' "
                     "10 May 2016.")
                print(s)
                # 10.0.14393 is "The Anniversary Update". Released 2 Aug 2016.
                print("Exiting...")
                sys.exit()
        if int(platform.release()) >= 10:
            # import ctypes
            kernel32 = ctypes.windll.kernel32
            status = kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            if status == 0:
                print("Error returned attempting to set ANSI escape sequences")
                print("Continuing, but results are not predictable...")
            else:
                s = "Windows has been set to perform ANSI escape sequences.\n"
                if debug: print(s)
                s = ("For more information on Microsoft use of ANSI escape"
                     "codes\nplease visit this web-page...\n"
                     "https://msdn.microsoft.com/en-us/library/mt638032"
                     "(v=vs.85).aspx")
                if debug: print(s)
        if delay: time.sleep(2)
        if pause: input("\nType Return key to continue")
    else:
        # The Linux platform normally has a console terminal that supports ANSI
        # escape sequences.
        pass


def draw_rectangle(start_column=1, start_row=1, width=80, height=24,
                   foreground_colour=39, background_colour=49):
    """
    Draw a rectangle using characters from Box Drawing character set.
    0x2500 to 0x257f
    Single top and single side from box drawing character set.
    ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

    # start_column = 1  # Columns (x-axis) start count at 1
    # start_row = 1  # Rows (y-axis) start count at 1 at top of screen.
    # width = 80  # Min. width = 2 Max greater than 80 columns then drop chars
    # height = 24  # Min. height = 2 Max of 24 or 25. But could be more.
    """
    # Execute function to check for valid colours and force correction
    foreground_colour, background_colour = colour_check(foreground_colour,
                                                        background_colour)
    # Set foreground and background colours
    print("{}{}m{}{}m".format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)

    # Top Line
    # Prints Left corner. E.g. at position 1. Then horizontal line. E.g. From
    # position 2 to column 79. Adds right corner. E.g. At position 80.
    print("{}{};{}H┌".format(CSI, start_row, start_column),
          end="", flush=True)
    for i in range(start_column + 1, start_column + width - 1):
        print("{}{};{}H─".format(CSI, start_row, i),
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
    # Prints bottom corner e.g. Position 1, then horizontal line. E.g. From
    # position 2 to column 79. Adds bottom corners. E.g. At position 80.
    print("{}{};{}H└".format(CSI, start_row + height - 1, start_column),
          end="", flush=True)
    for i in range(start_column + 1, start_column + width - 1):
        print("{}{};{}H─".format(CSI, start_row + height - 1, i),
              end="", flush=True)
    print("{}{};{}H┘"
          .format(CSI, start_row + height - 1, start_column + width - 1),
          end="", flush=True)

    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def colour_check(foreground_colour=39, background_colour=49):
    """
    Check colours are valid.
    If invalid colour set foreground to default of 39, and background to
    default of 49.
    To translate colour name strings to integers, use the COLOUR dictionary.
    Requires: COLOUR dictionary.
    """
    # print(COLOUR.keys())
    # print(COLOUR.values())
    if foreground_colour in COLOUR:
        # print(COLOUR[foreground_colour][0])
        foreground_colour = COLOUR[foreground_colour][0]
    if background_colour in COLOUR:
        # print(COLOUR[background_colour][1])
        background_colour = COLOUR[background_colour][1]
    # Check for if an invalid colour string was entered.
    try:
        int(foreground_colour)
        if (foreground_colour >= 30 and foreground_colour <= 37 or
            foreground_colour >= 90 and foreground_colour <= 97 or
                foreground == 39):
            # print("Foreground colour OK: {}".format(foreground_colour))
            pass
        else:
            # Foreground colour out of range, force it to be 97, i.e. white.
            # print("Foreground Out of range: {}".format(foreground_colour))
            foreground_colour = 39
    except:
        # Foreground colour is a string that is not a dictionary key.
        # Force the foreground to be the integer of white i.e. 97
        foreground_colour = 39

    # Check for if an invalid background colour string was entered.
    try:
        int(background_colour)
        if (background_colour >= 40 and background_colour <= 47 or
            background_colour >= 100 and background_colour <= 107 or
                background == 49):
            # print("background colour OK: {}".format(background_colour))
            pass
        else:
            # Background colour out of range, force it to be 40, i.e. black.
            # print("background Out of range: {}".format(background_colour))
            background_colour = 49
    except:
        # Background colour is a string that is not a dictionary key.
        # Force the background to be the integer of black i.e. 40
        background_colour = 49
    return foreground_colour, background_colour

    """
    # Check colour_check() code...
    fg,bg = colour_check(35,107)
    print(fg, bg)
    sys.exit()
    """


def write_text(text="", start_column=1, start_row=1, foreground_colour=39,
               background_colour=49):
    """
    Write text using x, y, foreground colour and background colour
    Using x,y order may overcome confusion of y,x in cursor addressing.
    E.g. Esc [ y x H Some text starting at y x cursor position.
    Print statement prohibits the newline with end="" and flush=True may
    overcome buffering issues.
    """
    # Execute function to check for valid colours and force correction
    foreground_colour, background_colour = colour_check(foreground_colour,
                                                        background_colour)

    # Apply foreground and background colours
    print("{}{}m{}{}m"
          .format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)

    # Apply direct cursor addressing and write the text.
    print("{}{};{}H{}".format(CSI, start_row, start_column, text),
          end="", flush=True)

    # Restore foreground (39) and background (49) colours to default values
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)


def write_field(text="", start_column=1, start_row=1, length=20, align="left",
                foreground_colour=39, background_colour=49):
    """
    Write field using x, y, length, alignment, foreground colour and
    background colour.
    Using x,y order may overcome confusion of y,x in cursor addressing.
    E.g. Esc [ y ; x H Some text starting at y x cursor position.
    Print statement prohibits the newline with end="" and flush=True may
    overcome buffering issues.
    The field length is provided. Text is alligned left, centre or right,
    in the field.
    """
    # Execute function to check for valid colours and force correction
    foreground_colour, background_colour = colour_check(foreground_colour,
                                                        background_colour)

    # Apply foreground and background colours
    print("{}{}m{}{}m"
          .format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)

    # Write a field of spaces for the length.
    space = " " * length
    print("{}{};{}H{}".format(CSI, start_row, start_column, space),
          end="", flush=True)

    # Align the text
    if align == "left":
        text = "{: <{}}".format(text, length)
    elif align == "centre":
        text = "{: ^{}}".format(text, length)
    elif align == "right":
        text = "{: >{}}".format(text, length)
    else:
        text = "{: <{}}".format(text, length)

    # Apply direct cursor addressing and write the text .
    print("{}{};{}H{}".format(CSI, start_row, start_column, text),
          end="", flush=True)

    # Restore foreground (39) and background (49) colours to default values
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)


if __name__ == "__main__":
    # Program starts here.
    main()

"""
Notes / Links:

http://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console

http://www.nivot.org/blog/post/2016/02/04/Windows-10-TH2-%28v1511%29-Console-Host-Enhancements

ANSI escape codes invoked by microsoft...
https://msdn.microsoft.com/en-us/library/mt638032(v=vs.85).aspx

Draw a rectangle using characters from Box Drawing character set.
0x2500 to 0x257f. Single top and single side from box drawing character set.
 ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

Support for Direct Cursor addressing CSI y ; x H
text = "Hello"
print("{}{};{}H{}".format(CSI, 22, 1, text), end="", flush=True)

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_23_e.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_23_e.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/

"""

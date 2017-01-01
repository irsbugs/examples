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
    Draw: Dummy form and Pizza Order form.
    Proceedural functions: main(), form_1(), pizza_form()
    Called functions()
    escape_sequence_check() - To check if Win10 is at the correct version
    draw_rectangle()
    draw_horizontal_line()
    draw_vertical_line()
    draw_intersection_line()
    colour_check() - Check if colour value is valid or translate text of
                     colour to numeric value.
    write_text() - Direct cursor addressing of text strings
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_23_d.py

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
    "Call the two forms"
    form_1()
    pizza_form()
    input("Press Enter key to end program")
    sys.exit()


def form_1():
    "Display a simple form using line drawing"
    # Check if it Windows 10 at correct version and turn on Escape sequences
    escape_sequence_check()

    print("{}2J".format(CSI))  # Clear screen

    # Draw main rectangle. default values are...
    x = 1
    y = 1
    width = 80
    height = 24
    f_colour = 39  # foreground use default value
    b_colour = 49  # background use default value
    # draw_rectangle(x, y, width, height, f_colour, b_colour)
    # Draw outside rectangle using defautl values
    draw_rectangle()

    if delay: time.sleep(delay_duration)
    draw_horizontal_line(1, 3)
    if delay: time.sleep(delay_duration)
    draw_horizontal_line(1, 22)
    if delay: time.sleep(delay_duration)

    # Draw vertical line in long form. Note:Width is ignored for vertical lines
    x = 20
    y = 3
    width = 80  # Ignored
    height = 20
    f_colour = 39
    b_colour = 49
    draw_vertical_line(x, y, width, height, f_colour, b_colour)

    draw_vertical_line(3, 3, 1, 20)

    draw_vertical_line(60, 3, 1, 22)
    if delay: time.sleep(delay_duration)

    # Add some data
    write_text("THE HEADING", 2, 2, "light_yellow")

    # Write numbers in left hand column
    for i in range(9):
        write_text(i + 1, 2, 4 + i, "white")

    write_text("The Last Line in a box - Yes?", 2, 23, "light_cyan")
    input()

    # Deleting in a line. The vertical drawing lines will get deleted
    # Microsoft documentation mixes up description for 0 and 1.
    # Below has been corrected...
    # 0. erases from the current cursor position (inclusive) to the end of the
    #    line/display
    # 1. erases from the beginning of the line/display up to and including the
    #    current cursor position
    # 2. erases the entire line/display.
    # print("{}{};{}H".format(CSI, 23,50,), end="", flush=True)
    # Set the cursor to a desired position in a line then delete up to cursor
    print("{}{};{}H{}{}K".format(CSI, 23, 15, CSI, 1), end="", flush=True)

    if pause: write_text("Messy huh?", 2, 23, "default", "default"); input()
    text = "Probably best to overwrite with spaces - Continue?"
    if pause: write_text(text, 2, 23, "default", "default"); input()


def pizza_form():
    "Display the pizza form"
    # Set the Console window title bar...
    # Note right square bracket - not left bracket - ESC ] 2 ; <string> BEL
    text = "Dream Pizza Company - Order Entry Form"
    print("{}]2;{}{}".format(ESC, text, BEL), end="", flush=True)
    print(BEL)

    # Eraze display
    print("{}2J".format(CSI), end="", flush=True)

    # Draw Rectangle and horizontal lines
    draw_rectangle()
    draw_horizontal_line(1, 3)
    draw_horizontal_line(1, 5)
    draw_horizontal_line(1, 22)

    # Vertical top lines
    draw_vertical_line(13, 1, 1, 3)
    draw_vertical_line(47, 1, 1, 3)
    draw_vertical_line(55, 1, 1, 3)

    # Line 2 data...
    # Logo
    write_text("DREAM PIZZA", 2, 2, "light_yellow")

    # Customer
    customer_name = "John Smith"  # 23 Character limit
    write_text("Customer: " + customer_name, 14, 2, "white")

    # Delivery: Deliver or Pickup
    pickup = "Deliver"
    write_text(pickup, 48, 2, "white")

    # Time stamp
    write_text(time.asctime(), 56, 2, "light_cyan")

    # Line 4 data...
    # Column No. field
    write_text("No.", 2, 4, "white")

    # Column Qty field
    draw_vertical_line(5, 3, 1, 20)
    write_text("Qty", 6, 4, "white")

    # Column Description field
    draw_vertical_line(9, 3, 1, 20)
    write_text("Description", 10, 4, "white")

    # Unit Price Unit $. Use format() for centering text.
    draw_vertical_line(60, 3, 1, 20)
    text = "{: ^8}".format("Unit $")
    write_text(text, 61, 4, "white")

    # Total Price $. Use format() for centering text.
    draw_vertical_line(70, 3, 1, 22)
    text = "{: ^8}".format("Totals $")
    write_text(text, 71, 4, "white")

    # Line 23 data...
    # Total Amount $
    write_text("Total Amount", 58, 23, "white")

    # Dummy data
    data = (["1", "2", "Hawaiian", "$8.50", "$17.00"],
            ["2", "1", "Double Cheese", "$8.50", "$8.50"],
            ["3", "1", "Meat Lovers", "$8.50", "$8.50"],
            ["4", "1", "Delivery: 100 Hillcrest Rd. ph.0-211-111-222-333",
             "$3.00", "$3.00"]
            )
    data_total = "$37.00"

    # Add data
    for index, item in enumerate(data):
        write_text(item[0], 3, index + 6, "white")
        write_text(item[1], 7, index + 6, "white")
        write_text(item[2], 11, index + 6, "white")
        write_text("{: >8}".format(item[3]), 61, index + 6, "white")
        write_text("{: >8}".format(item[4]), 71, index + 6, "white")

    write_text("{: >8}".format(data_total), 71, 23, "light_yellow")

    # Add the cross-hairs where lines intersect.
    # In Win10 this fails to display correctly and displays a square.
    # Use a tuple of column and row value pairs for position of cross-hairs.
    intersection = ((5, 5), (9, 5), (60, 5), (70, 5), (70, 22))
    for index, data in enumerate(intersection):
        draw_intersection_line(data[0], data[1])

    write_text("Customer Confirms Order (Y/n)? [Yes]: ", 2, 23, "light_cyan")
    return_string = input()
    if not return_string:
        return_string = "Yes"

    # Write 50 spaces to clear text. Prevents overwriting the line drawing.
    text = " " * 50
    write_text(text, 2, 23,)
    if delay: time.sleep(1)

    # Display the returned value and exit.
    text = ("Returned string:{}. Type Return to end program."
            .format(return_string))
    if pause: write_text(text, 2, 23, "white"); input()


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


def draw_horizontal_line(start_column=1, start_row=1, width=80, height=24,
                         foreground_colour=39, background_colour=49):
    """
    Draw a horizontal line with t-sections at each end
    Single top and single side from box drawing character set.
    ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
    """
    # Execute function to check for valid colours and force correction
    foreground_colour, background_colour = colour_check(foreground_colour,
                                                        background_colour)
    # Set foreground and background colours and turn on line drawing
    print("{}{}m{}{}m"
          .format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)

    # T-Section at left end of the line.
    print("{}{};{}H├".format(CSI, start_row, start_column), end="", flush=True)
    # Horizontal line.
    for i in range(start_column + 1, start_column + width - 1):
        print("{}{};{}H─".format(CSI, start_row, i), end="", flush=True)
    # T-Section at right end of the line.
    print("{}{};{}H┤".format(CSI, start_row, start_column + width - 1),
          end="", flush=True)

    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def draw_vertical_line(start_column=1, start_row=1, width=80, height=24,
                       foreground_colour=39, background_colour=49):
    """
    Draw a vertical line with t-sections at each end
    Single top and single side from box drawing character set.
    ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
    """
    # Execute function to check for valid colours and force correction
    foreground_colour, background_colour = colour_check(foreground_colour,
                                                        background_colour)
    # Set foreground and background colours and turn on line drawing
    print("{}{}m{}{}m".format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)

    # Add the top t-section
    print("{}{};{}H┬".format(CSI, start_row, start_column), end="", flush=True)
    # Draw vertical line
    for i in range(start_row + 1, start_row + height - 1):
        print("{}{};{}H│".format(CSI, i, start_column), end="", flush=True)
    # Add the bottom t-section
    print("{}{};{}H┴".format(CSI, start_row + height - 1, start_column),
          end="", flush=True)

    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def draw_intersection_line(start_column=1, start_row=1, width=1, height=1,
                           foreground_colour=39, background_colour=49):
    """
    Draw an intersection cross-hairs line
    Single top and single side from box drawing character set.
    ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
    """
    # Execute function to check for valid colours and force correction
    foreground_colour, background_colour = colour_check(foreground_colour,
                                                        background_colour)
    # Set foreground and background colours and turn on line drawing
    print("{}{}m{}{}m".format(CSI, foreground_colour, CSI, background_colour),
          end="", flush=True)
    # Set the position and insert the cross-hairs.
    print("{}{};{}H┼".format(CSI, start_row, start_column), end="", flush=True)
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


if __name__ == "__main__":
    # Program starts here.
    main()

"""
Notes / Links:

http://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console

http://www.nivot.org/blog/post/2016/02/04/Windows-10-TH2-%28v1511%29-Console-Host-Enhancements

Draw a rectangle using characters from Box Drawing character set.
0x2500 to 0x257f. Single top and single side from box drawing character set.
 ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

ANSI escape codes invoked by microsoft...
https://msdn.microsoft.com/en-us/library/mt638032(v=vs.85).aspx

Support for Direct Cursor addressing CSI y ; x H
text = "Hello"
print("{}{};{}H{}".format(CSI, 22, 1, text), end="", flush=True)

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

# Display all 16 colours as bars. Each colour is 4 char positions wide.
# Draw as a two rectangles. A rectangle with a smaller rectangle inside.
# Numeric values for foreground and background colours. CSI<colour value>m
foreground = (30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97)
background = (40, 41, 42, 43, 44, 45, 46, 47, 100, 101, 102, 103, 104, 105,
              106, 107)

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_23_d.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_23_d.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/

"""

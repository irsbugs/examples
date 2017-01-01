#!/usr/bin/env python3
#
import sys
import time
import datetime
import platform
import ctypes

_description_ = """
    Making use of Direct Cursor addressing, and colour.
    Line Drawing is part of the ASCII character set.
    Does not require ANSI escape sequences to perform the drawing.
    Supported on Windows 10 patched to May 2016 revision or later.
    Uses methods for each line drawing graphic character. Uses single line.

    Procedural functions: main(),
    setup_initial_screen(), get_continue(), get_first_name(), get_surname(),
    get_gender(), get_age(), get_fruit(), get_drink(), insert_time(), and
    generate_report(data_list).
    escape_sequence_check() - To check if Win10 is at the correct version.
    colour_check() - Check if colour value is valid or translate text of
                     colour to numeric value.
    write_text() - Direct cursor addressing of text strings
    write_field() - Includes length and alignment of text in the field
    menu_selection() - Provide a sub-menu in the middle of the screen
    clear_area() - Clear the sub menu
    clear_line_23() - Line 23 is used for input
    get_integer() - Get integer value from user
    get_string() - Get string from user.

    Main methods for drawing boxes. These call the 11 x methods below
    draw_box(), draw_box_horizontal(), draw_box_vertical
    11 x methods are included to be called by other methods for line drawing.
    Colour checking and turning on/off line drawing is not performed.
    draw_horizontal(), draw_vertical()
    draw_top_left(), draw_top_right(), draw_bottom_left(), draw_bottom_right()
    draw_top_t(), draw_bottom_t(), draw_left_t(), draw_right_t()
    draw_intersection()
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_24_c.py

# Global Constants:
# delay, debug and pause are only used in enabling Windows 10 ANSI sequences.
delay = True
debug = True
pause = True

ESC = chr(27)  # Escape character
CSI = ESC + "["  # Control Sequence Introducer
BEL = chr(7)  # Bell

WELCOME = "\nWelcome to the ANSI Escape Sequences program."

MENU_1 = ("Continue...", "Exit Program")

MENU_2 = ("Male", "Female")

MENU_3 = ("0-9", "10 to 19", "20 to 29", "30 to 39", "40 to 49", "50 to 59",
          "60 to 69", "70 to 79", "80 to 89", "90 to 99")

MENU_4 = ("Apple", "Pear", "Cherry", "Grape", "Avocado", "Banana",
          "Watermelon", "Raspberry", "Fig", "Pineapple", "Orange", "Kiwifruit")

MENU_5 = ("Water", "Orange", "Lemon", "Lime", "Coffee", "Tea", "Milk", "Soda")

MENU_6 = ("Yes", "No")

# Colour constants
BACKGROUND = "dark_blue"
FOREGROUND = "light_yellow"
LINE_FORE = "white"
LINE_BACK = "dark_blue"
LINE_23_FORE = "white"
LINE_23_BACK = "red"
MENU_FORE = "light_green"
MENU_BACK = "green"
TEXT_FORE = "white"
REPORT_FORE = "red"
REPORT_BACK = "light_yellow"
REPORT_TEXT = "black"
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
    """
    main procedural function to control flow of program
    call functions to perform tasks.
    """
    # Local variables
    delivery_charge = False

    # If Win10 check version supports ANSI escape sequences.
    escape_sequence_check()

    # Set console window title bar.
    # This Operating System Command (OSC) may be only valid for Windows 10.
    text = "ANSI sequences. Data entry program"
    print("{}]2;{}{}".format(ESC, text, BEL), end="", flush=True)
    print(BEL)

    while True:
        # Setup initial screen...
        setup_initial_screen()

        # Continue or exit program...
        get_continue()

        # Get infromation...
        firstname = get_first_name()

        surname = get_surname()

        gender = get_gender()

        age = get_age()

        fruit = get_fruit()

        drink = get_drink()

        time_stamp = insert_time()

        # Build data list for use in displaying report
        data_list = [("First name", firstname),
                     ("Surname", surname),
                     ("Gender", gender),
                     ("Age Group", age),
                     ("Favourite Fruit", fruit),
                     ("Favourite Drink", drink),
                     ("Time", time_stamp)]

        generate_report(data_list)


def setup_initial_screen():
    """
    Define foreground and background colours.
    Clear screen to set background colour.
    Draw main boxes and lines and add text.
    """
    # Set default colours
    foreground_colour, background_colour = colour_check(FOREGROUND, BACKGROUND)
    print("{}{}m".format(CSI, foreground_colour))
    print("{}{}m".format(CSI, background_colour))
    # Clear screen - applies background colour
    print("{}2J".format(CSI))

    # Draw main rectangle
    draw_box(1, 1, 80, 24, LINE_FORE, LINE_BACK)

    # Draw horizontal line on lines 5 and 22
    draw_box_horizontal(1, 3, 80, 1, LINE_FORE, LINE_BACK)
    draw_box_horizontal(1, 5, 80, 1, LINE_FORE, LINE_BACK)
    draw_box_horizontal(1, 22, 80, 1, LINE_FORE, LINE_BACK)

    # Vertical lines first row
    draw_box_vertical(20, 1, 1, 5, LINE_FORE, LINE_BACK)
    draw_box_vertical(40, 1, 1, 5, LINE_FORE, LINE_BACK)
    draw_box_vertical(60, 1, 1, 5, LINE_FORE, LINE_BACK)

    # Intersections on line 3
    draw_intersection_line(20, 3, 1, 1, LINE_FORE, LINE_BACK)
    draw_intersection_line(40, 3, 1, 1, LINE_FORE, LINE_BACK)
    draw_intersection_line(60, 3, 1, 1, LINE_FORE, LINE_BACK)

    # Add initial text...
    write_field("ANSI Sequences", 2, 2, 18, "centre", FOREGROUND, BACKGROUND)
    write_field("First Name", 21, 2, 18, "centre", FOREGROUND, BACKGROUND)
    write_field("Surname", 41, 2, 18, "centre", FOREGROUND, BACKGROUND)
    write_field("Male / Female", 61, 2, 18, "centre", FOREGROUND, BACKGROUND)

    write_field("Age Range", 2, 4, 18, "centre", FOREGROUND, BACKGROUND)
    write_field("Fruit", 21, 4, 18, "centre", FOREGROUND, BACKGROUND)
    write_field("Drink", 41, 4, 18, "centre", FOREGROUND, BACKGROUND)
    write_field("Time", 61, 4, 18, "centre", FOREGROUND, BACKGROUND)


def get_continue():
    """
    Determine whether to continue exit the program?
    Function uses MENU_1 tuple.
    Calls menu_selection()
    Passes MENU_1 tuple, in which length is used to draw menu
    Clear menu and Selection line #23.
    If exiting, then restore default colours and clear screen.
    """
    # Draw the menu selection
    menu_selection("Menu_1 - Continue...", MENU_1)
    value = get_integer("Enter selection", "0", len(MENU_1) - 1)
    # Clear the menu and the selection line
    clear_area(20, 6, 40, 15, BACKGROUND, BACKGROUND)
    clear_line_23()
    # print(value)
    if value == 1:
        # Clean-up and exit program...
        text = "Program exiting..."
        write_field(text, 2, 23, 78, "centre", FOREGROUND, BACKGROUND)
        time.sleep(2)
        # Restore default foreground / background colours
        print("{}39m".format(CSI))
        print("{}49m".format(CSI))
        # Clear screen
        print("{}2J".format(CSI))
        print("{}{};{}H".format(CSI, 1, 1, text), end="", flush=True)
        input("Press Enter key to end program")
        sys.exit()
    else:
        # Continue and start getting details.
        pass
    return value


def get_first_name():
    """
    Get first name
    Calls: get_string()
    """
    name = get_string("Enter First Name")
    write_field(name, 21, 2, 18, "left", FOREGROUND, BACKGROUND)
    return name


def get_surname():
    """
    Get surname
    Calls: get_string()
    """
    name = get_string("Enter Surname")
    write_field(name, 41, 2, 18, "left", FOREGROUND, BACKGROUND)
    return name


def get_gender():
    """
    Get the gender
    Function uses MENU_2 tuple.
    Calls menu_selection()
    Passes MENU_2 tuple, in which length is used to draw menu
    Clear menu and Selection line #23.
    """
    # Draw the menu selection
    menu_selection("Menu_2 - Gender", MENU_2)
    value = get_integer("Select Gender", "0", len(MENU_1) - 1)
    if value == 0:
        gender = "Male"
    else:
        gender = "Female"
    write_field(gender, 61, 2, 18, "left", FOREGROUND, BACKGROUND)
    # Clear the menu and the selection line
    clear_area(20, 6, 40, 15, BACKGROUND, BACKGROUND)
    clear_line_23()
    return gender


def get_age():
    """
    Get the age range
    Function uses MENU_3 tuple.
    Calls menu_selection()
    Passes MENU_3 tuple, in which length is used to draw menu
    Clear menu and Selection line #23.
    """
    # Draw the menu selection
    menu_selection("Menu_3 - Age Group in Years", MENU_3)
    value = get_integer("Select Age Range", "0", len(MENU_3) - 1)
    age = MENU_3[value] + " years"
    write_field(age, 2, 4, 18, "left", FOREGROUND, BACKGROUND)
    # Clear the menu and the selection line
    clear_area(20, 6, 40, 15, BACKGROUND, BACKGROUND)
    clear_line_23()
    return age


def get_fruit():
    """
    Get favourite fruit
    Function uses MENU_4 tuple.
    Calls menu_selection()
    Passes MENU_4 tuple, in which length is used to draw menu
    Clear menu and Selection line #23.
    """
    # Draw the menu selection
    menu_selection("Menu_4 - Favourite Fruit", MENU_4)
    value = get_integer("Select Favourite Fruit", "0", len(MENU_4) - 1)
    fruit = MENU_4[value]
    write_field(fruit, 21, 4, 18, "left", FOREGROUND, BACKGROUND)
    # Clear the menu and the selection line
    clear_area(20, 6, 40, 15, BACKGROUND, BACKGROUND)
    clear_line_23()
    return fruit


def get_drink():
    """
    Get favourite drink
    Function uses MENU_5 tuple.
    Calls menu_selection()
    Passes MENU_5 tuple, in which length is used to draw menu
    Clear menu and Selection line #23.
    """
    # Draw the menu selection
    menu_selection("Menu_5 - Favourite Drink", MENU_5)
    value = get_integer("Select Favourite Drink", "0", len(MENU_5) - 1)
    drink = MENU_5[value]
    write_field(drink, 41, 4, 18, "left", FOREGROUND, BACKGROUND)
    # Clear the menu and the selection line
    clear_area(20, 6, 40, 15, BACKGROUND, BACKGROUND)
    clear_line_23()
    return drink


def insert_time():
    """
    Insert a time stamp of the desired style
    """
    time_style = ("DD-MM-YY HH:MM:SS",
                  "YY-MM-DD HH:MM:SS",
                  "DD-MMM-YY HH:MM:SS",
                  "YYMMDD.HHMMSS")

    time_syntax = ("%d-%m-%y %H:%M:%S",
                   "%y-%m-%d %H:%M:%S",
                   "%d-%b-%y %H:%M:%S",
                   "%y%m%d.%H%M%S")

    # Draw the menu selection
    menu_selection("Time Stamp Style Menu", time_style)
    value = get_integer("Select Time stamp Style", "0", len(time_style) - 1)
    time_type = time_syntax[value]
    time_stamp = datetime.datetime.now().strftime(time_type)
    write_field(time_stamp, 61, 4, 18, "left", FOREGROUND, BACKGROUND)
    # Clear the menu and the selection line
    clear_area(20, 6, 40, 15, BACKGROUND, BACKGROUND)
    clear_line_23()
    return time_stamp


def generate_report(data_list):
    """
    Function uses MENU_6 tuple.
    Calls menu_selection()
    Passes MENU_6 tuple, in which length is used to draw menu
    Clear menu and Selection line #23.
    """
    # Draw the menu selection
    menu_selection("Menu_6 - Generate Report?", MENU_6)
    value = get_integer("Select Report Generation", "0", len(MENU_6) - 1)
    # Clear the menu and the selection line
    clear_area(20, 6, 40, 15, BACKGROUND, BACKGROUND)
    clear_line_23()
    # print(value)

    if value == 0:
        # Yes - Display report
        # print(data_list)
        display_report("Information Report", data_list)

    write_field("Type Return to continue", 2, 23, 78, "left", LINE_23_FORE,
                LINE_23_BACK)
    input()  # Pause the program.
    # Clear the menu and the selection line
    clear_area(20, 6, 40, 15, BACKGROUND, BACKGROUND)
    clear_line_23()
    return value


def display_report(title="Title", description=("stuff", "more stuff")):
    """
    Draws a box in the middle of the screen with a title.
    Has selection numbering in left column and descriptions in right column.
    Passed: Title string, and Description list of keyword and argument.
    Based on length of Description list determines size of box.
    """
    x = 20
    y = 6
    width = 40
    height = len(description) + 4

    # Draw menu rectangle
    draw_box(x, y, width, height, REPORT_FORE, REPORT_BACK)

    # Draw horizontal line top
    draw_box_horizontal(x, y + 2, width, 1, REPORT_FORE, REPORT_BACK)
    # Draw vertical line
    draw_box_vertical(x + 3, y + 2, 1, height - 2, REPORT_FORE, REPORT_BACK)

    write_field(title, x + 1, y + 1, width - 2, "centre", REPORT_TEXT,
                REPORT_BACK)

    for index, item in enumerate(description):
        item = "{: <15} {: <19}".format(item[0], item[1])

        write_field(str(index + 1), x + 1, y + 3 + index, 2, "right",
                    REPORT_TEXT, REPORT_BACK)
        write_field(item, x + 4, y + 3 + index, width - 5, "left",
                    REPORT_TEXT, REPORT_BACK)


# End of methods called by main()
# Start of miscellaneous utility functions...

def menu_selection(title="Title", description=("stuff", "more stuff")):
    """
    Draws a box in the middle of the screen with a title.
    Has selection numbering in left column and descriptions in right column.
    Passed: Title string, and Description tuple.
    Based on length of Description tuple determines size of box.
    """
    x = 20
    y = 6
    width = 40
    height = len(description) + 4
    # Draw menu rectangle
    draw_box(x, y, width, height, MENU_FORE, MENU_BACK)

    # Draw horizontal line top
    draw_box_horizontal(x, y + 2, width, 1, MENU_FORE, MENU_BACK)
    # Draw vertical line
    draw_box_vertical(x + 3, y + 2, 1, height - 2, MENU_FORE, MENU_BACK)

    write_field(title, x + 1, y + 1, width - 2, "centre", TEXT_FORE, MENU_BACK)

    for index, item in enumerate(description):
        write_field(str(index), x + 1, y + 3 + index, 2, "right",
                    TEXT_FORE, MENU_BACK)
        write_field(item, x + 4, y + 3 + index, width - 5, "left",
                    TEXT_FORE, MENU_BACK)


def clear_line_23(fore_colour=LINE_23_FORE, back_colour=LINE_23_BACK):
    """
    Clear selection line #23 and set cursor to Line 23 position 2
    Set the colours
    """
    # Execute function to check for valid colours and force correction
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Set foreground and background colours.
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour, ESC),
          end="", flush=True)
    # Clear line 23 by writing spaces to the line
    text = " " * 78
    print("{}{};{}H{}".format(CSI, 23, 2, text), end="", flush=True)
    print("{}{};{}H".format(CSI, 23, 2), end="", flush=True)
    # Restore foreground and background colours.
    # and move cursor to 1,1 to prevent screen scrolling if 23 row
    # print("{}39m{}49m{}{};{}H".format(CSI, CSI, CSI, 1, 1),
    #      end="", flush=True)


def get_integer(text="Enter an integer", prompt="0", maximum=0):
    """
    Routine to retrieve an integer from the User keyboard.
    A prompt value is provided.
    Integer is forced to be positive.
    The integer can not be larger than specificed maximum value
    """
    while True:
        clear_line_23()
        response = input("{} [{}]: ".format(text, prompt))
        if not response:
            response = prompt
        try:
            integer = abs(int(response))
            if integer > maximum:
                # print("Invalid entry. Please re-enter...")
                continue
            else:
                return integer
        except ValueError as e:
            # TODO: Display error message for 1 second then continue
            # print("Value Error: {}".format(e))
            # print("Invalid entry. Please re-enter...")
            continue


def get_string(text="Enter a string", prompt=None):
    """
    Routine to retrieve a string fron the User keyboard.
    A prompt is available. If prompt supplied, allow Return to accept prompt.
    If no prompt then force user to supply a response.
    """
    if prompt:
        clear_line_23()
        response = input("{} [{}]: ".format(text, prompt))
        if not response:
            response = prompt
        return response
    else:
        while True:
            clear_line_23()
            response = input("{}: ".format(text))
            if not response:
                # print("Nothing entered. Please type an entry...")
                continue
            else:
                return response


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


def draw_box(x=1, y=1, width=80, height=24, fore_colour=39, back_colour=49):
    """
    Draw a rectangle.
    Use the calls to the drawing methods.
    """
    # Call check for valid colours and force correction if required
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Set foreground and background colours
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)

    # Top line
    # Prints horizontal line. E.g. From position 2 to column 79
    for i in range(x + 1, x + width - 1):
        draw_horizontal(i, y)

    # Adds corners. E.g. At positions 1 and 80.
    draw_top_left(x, y)
    draw_top_right(x + width - 1, y)

    # Draw middle lines
    # Adds the vertical lines on each side of the box. Positions 1 and 80
    for i in range(y + 1, y + height - 1):
        draw_vertical(x, i)
        draw_vertical(x + width - 1, i)

    # Bottom line
    # Prints horizontal line. E.g. From position 2 to column 79
    for i in range(x + 1, x + width - 1):
        draw_horizontal(i, y + height - 1)
    # Adds corners. E.g. At positions 1 and 80.
    draw_bottom_left(x, y + height - 1)
    draw_bottom_right(x + width - 1, y + height - 1)

    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def draw_box_horizontal(x=1, y=1, width=80, height=1, fore_colour=39,
                        back_colour=49):
    """
    Draw a horizontal line in a box. i.e. have t-sections at the ends
    Height argument is ignored
    """
    # Call check for valid colours and force correction if required
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Set foreground and background colours
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)

    # Horizontal line.
    for i in range(x + 1, x + width - 1):
        draw_horizontal(i, y)
    # T-Sections at each end of the line.
    draw_left_t(x, y)
    draw_right_t(x + width - 1, y)

    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def draw_box_vertical(x=1, y=1, width=1, height=24, fore_colour=39,
                      back_colour=49):
    """
    Draw a vertical line in a box. i.e. have t-sections at the ends
    Width argument is ignored.
    """
    # Call check for valid colours and force correction if required
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Set foreground and background colours and turn on line drawing
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)

    # Draw vertical line
    for i in range(y + 1, y + height - 1):
        draw_vertical(x, i)
    # Add the t-sections at the top and bottom of the line
    draw_top_t(x, y)
    draw_bottom_t(x, y + height - 1)

    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def clear_area(x=1, y=1, width=80, height=24, fore_colour=39, back_colour=49):
    """
    Clear an area of the screen by overwriting sections of a line
    with spaces
    """
    # Execute function to check for valid colours and force correction
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Replace area with spaces, thus applying backcolour.
    for i in range(height + 1):
        for j in range(width + 1):
            print("{}{}m{}{};{}H ".format(CSI, back_colour, CSI, y + i, x + j),
                  end="", flush=True)


def draw_bottom_left_corner(x=1, y=1, width=1, height=1, fore_colour=39,
                            back_colour=49):
    """
    Not used by this program.
    Draw the bottom left hand corner.
    width and height are ignored.
    """
    # Execute function to check for valid colours and force correction
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Set foreground and background colours and turn on line drawing
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)
    # Draw bottom left right angle. Line drawing character "m".
    draw_bottom_left(x, y)
    # Restore foreground and background colours.
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def draw_bottom_t_section(x=1, y=1, width=1, height=1, fore_colour=39,
                          back_colour=49):
    """
    Not used by this program
    Draw the bottom line t's
    Width and height are ignored.
    """
    # Execute function to check for valid colours and force correction
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Set foreground and background colours and turn on line drawing
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)
    # Draw inverted t's. Line drawing character "v".
    draw_bottom_t(x, y)
    # Turn off line drawing and restore foreground and background colours.
    # and move cursor to 1,1 to prevent screen scrolling if 23 row
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def draw_vertical_bar(x=1, y=1, width=1, height=1, fore_colour=39,
                      back_colour=49):
    """
    Not used by this program
    Draw a vertical line at a single character cell position
    Width and Height are ignored.
    """
    # Execute function to check for valid colours and force correction
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Set foreground and background colours and turn on line drawing
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)
    # Draw vertical bar. Line drawing character "x"
    draw_vertical(x, y)
    # Turn off line drawing and restore foreground and background colours.
    # and move cursor to 1,1 to prevent screen scrolling if 23 row
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)
    return 0


def draw_intersection_line(x=1, y=1, width=1, height=1, fore_colour=39,
                           back_colour=49):
    """
    Draw intersection lines / cross-hairs symbol.
    Width and height are ignored.
    """
    # Execute function to check for valid colours and force correction
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Set foreground and background colours and turn on line drawing
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)
    # Insert the cross-hairs. Line drawing character "n"
    draw_intersection(x, y)
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


def write_text(text="", x=1, y=1, fore_colour=39, back_colour=49):
    """
    Write text using x, y, foreground colour and background colour
    Using x,y order may overcome confusion of y,x in cursor addressing.
    E.g. Esc [ y x H Some text starting at y x cursor position.
    Print statement prohibits the newline with end="" and flush=True may
    overcome buffering issues.
    """
    # Execute function to check for valid colours and force correction
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Apply foreground and background colours
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)
    # Apply direct cursor addressing and write the text.
    print("{}{};{}H{}".format(CSI, y, x, text), end="", flush=True)
    # Restore foreground (39) and background (49) colours to default values
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)


def write_field(text="", x=1, y=1, length=20, align="left", fore_colour=39,
                back_colour=49):
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
    fore_colour, back_colour = colour_check(fore_colour, back_colour)
    # Apply foreground and background colours
    print("{}{}m{}{}m".format(CSI, fore_colour, CSI, back_colour),
          end="", flush=True)
    # Write a field of spaces for the length.
    space = " " * length
    print("{}{};{}H{}".format(CSI, y, x, space), end="", flush=True)
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
    print("{}{};{}H{}".format(CSI, y, x, text), end="", flush=True)
    # Restore foreground (39) and background (49) colours to default values
    print("{}39m{}49m".format(CSI, CSI), end="", flush=True)


# 11 x methods to draw the lines.
# No colour checking is performed.
# Line drawing
# ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
def draw_horizontal(x=1, y=1):
    """Draw the horizontal bar. Used in horizontal lines. i.e. q """
    print("{}{};{}H─".format(CSI, y, x), end="", flush=True)


def draw_vertical(x=1, y=1):
    """Draw the vertical bar. Used in vertical lines. i.e. x """
    print("{}{};{}H│".format(CSI, y, x), end="", flush=True)


def draw_top_left(x=1, y=1):
    """Draw the top left corner. i.e. l """
    print("{}{};{}H┌".format(CSI, y, x), end="", flush=True)


def draw_top_right(x=1, y=1):
    """Draw the top right corner. i.e. k """
    print("{}{};{}H┐".format(CSI, y, x), end="", flush=True)


def draw_bottom_left(x=1, y=1):
    """Draw the bottom left corner. i.e. m """
    print("{}{};{}H└".format(CSI, y, x), end="", flush=True)


def draw_bottom_right(x=1, y=1):
    """Draw the top left corner. i.e. j """
    print("{}{};{}H┘".format(CSI, y, x), end="", flush=True)


def draw_top_t(x=1, y=1):
    """Draw the top t section. i.e. w """
    print("{}{};{}H┬".format(CSI, y, x), end="", flush=True)


def draw_bottom_t(x=1, y=1):
    """Draw the bottom t section. i.e. v """
    print("{}{};{}H┴".format(CSI, y, x), end="", flush=True)


def draw_left_t(x=1, y=1):
    """Draw the left t section. i.e. t """
    print("{}{};{}H├".format(CSI, y, x), end="", flush=True)


def draw_right_t(x=1, y=1):
    """Draw the right t section. i.e. u """
    print("{}{};{}H┤".format(CSI, y, x), end="", flush=True)


def draw_intersection(x=1, y=1):
    """Draw the intersection / crosshairs section. i.e. n. Fails on Windows"""
    print("{}{};{}H┼".format(CSI, y, x), end="", flush=True)


if __name__ == "__main__":
    main()

"""
Notes / Links:

http://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console

http://www.nivot.org/blog/post/2016/02/04/Windows-10-TH2-%28v1511%29-Console-Host-Enhancements

ANSI escape codes invoked by microsoft...
https://msdn.microsoft.com/en-us/library/mt638032(v=vs.85).aspx

http://www.unicode.org/charts/PDF/U2500.pdf
Range: 2500–257F

Line Drawing as part of character set.
Single horizontal and vertical
─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

Double horizontal and vertical
═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬

Double horizontal, Single vertical
═ │ ╒ ╕ ╘ ╛ ╞ ╡ ╤ ╧ ╪

Single horizontal, Double vertical
─ ║ ╓ ╖ ╙ ╜ ╟ ╢ ╥ ╨ ╫

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_24_c.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_24_c.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/

"""

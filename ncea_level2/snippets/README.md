# Code Snippets for Python - Level 2
Links: [Github](https://github.com/irsbugs/examples/blob/master/ncea_level2/snippets/README.md) or [Website](https://irsbugs.github.io/examples/ncea_level2/snippets/) 

These code snippets may be useful for anyone who is learning the Python programming language. Their level of complexity is to encourage the use of the procedural programming style. They highlight development of function code blocks, but do not cover developing classes. They also assume the program is written as one file, and importing of modules is restricted to a small set of the builtin python modules. 

The programs are all console terminal based and there is no use of GUI windowing. Linux and Windows10 (with TH2 update kit) console terminal windows support ANSI 3.64 escape sequences. This allows direct cursor addressing and setting foreground and backgound colours of each character cell. Also the unicode Box Drawing graphic characters are supported. Some of these snippet programs highlight these features.

The snippets were developed using Python 3.4. They have been tested on Ubuntu Linux and Windows10 desktop environments.

New Zealand secondary school teachers and students may find these snippets useful for the Digital Technologies, Level 2, Achievement Standards [91372](http://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2017/as91372.pdf) and [91373](http://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2017/as91373.pdf).

In a classroom computer lab that uses Windows10 desktop computers, the console terminal window applications (CMD and Powershell) may have been made unavailable on the students desktop computers. In the Windows10 file manager, if a *python* file is double-clicked it will launch a terminal window to run the python program. When the program completes, this terminal window is closed. To prevent the programs closing before a student has been able to see what the program does, all these snippet programs end with the lines...

    
    input("Press Enter key to end the program.")
    sys.exit()
    

Below is a list of the snippet programs and a brief description of their functionality.


**snip_l2_01_a.py**

    Import time and use sleep() for 5 seconds.
    
**snip_l2_01_b.py**

    Import time and use sleep() for the amount of time in seconds specified
    by the constant 'S'.
    Uses .format() function with print().
    
**snip_l2_01_c.py**

    Import time and use sleep() for the the number of seconds of the 'DELAY'
    constant. DELAY is a more meaningful name to the constant than using the
    letter 'S'.
    Uses .format() function with print().
    
**snip_l2_01_d.py**

    Import time and use sleep() for the the number of seconds of the 'delay'
    variable. The input() function is used to get the desired delay from the
    user.
    Uses .format() function with print().
    
**snip_l2_01_e.py**

    Import time and use sleep() for the the number of seconds of the
    'DELAY_IN_SECS' constant.
    Define a function to perform the delay. Note that within the
    function it can use the DELAY_IN_SECS constant that was previously set
    outside of the function. i.e. The function does not require being passed
    the DELAY_IN_SEC constant.
    Uses .format() function with print().
    
**snip_l2_01_f.py**

    Introduce procedural programming style.
    Use if __name__ == "__main__": to start the program and call the main()
    function.
    Uses .format() function with print().
    The first argument of the list sys.argv, i.e. sys.argv[0] is the programs
    name. i.e. snip_l2_01_e.py
    The time.sleep(5) provides a 5 second delay.
    
**snip_l2_02_a.py**

    Import time and sleep for the number of seconds of the 'DELAY_IN_SECS'
    constant. Log the start and end of the program to a logging file.
    Use log_file = open(), log_file.write() and log_file.close()
    Simple flow programming style.
    
**snip_l2_02_b.py**

    Import time and use sleep() for the number of seconds of the
    'DELAY_IN_SECS' constant.
    Log the start and end of the program to a log file. Use 'with'
    in opening output file which means the log_file.close() is not required.
    Simple flow programming style.
    
**snip_l2_02_c.py**

    Import time and use sleep() for the number of seconds of the
    'DELAY_IN_SECS' constant.
    Use a function to log the start and end of the program to a logging file.
    
**snip_l2_03_a.py**

    Import time and use sleep(1) for one second intervals to provide a
    countdown. Use a for loop. Need to subtract from 5 to countdown to 0.
    
**snip_l2_03_b.py**

    Import time and sleep for one second to provide a countdown.
    Use for loop. Use reversed() on the range() to count down to 0.
    
**snip_l2_03_c.py**

    Import time and sleep for one second to provide a countdown.
    Use for loop. Call a function to to print the countdown.
    
**snip_l2_03_d.py**

    Import time and use sleep() for one second to provide a countdown.
    Use for loop. Call a print function. Use plural seconds, and singular
    on 1 second.
    
**snip_l2_04_a.py**

    Use default integer value or get a string value from the command line.
    Use three methods, type comparison, isinstance() and try/except.
    
**snip_l2_05_a.py**

    Use input () function to get data from the User at the command line.
    Use while True loop to ensure data is entered or data is of the desired
    type.
    
**snip_l2_05_b.py**

    Use input () function to get data from the User at the command line.
    Use while True loop to ensure data is entered or data is of the desired
    type.
    Apply format() function to the input() function.
    Simple flow programming style.
    
**snip_l2_05_c.py**

    Define a function to get data from the User at the command line.
    Use while True loop to ensure data is entered or data is of the desired
    type.
    Apply format() function to the input() function.
    Read the global constants TEXT and PROMPT rather than pass them to
    function.
    Simple flow programming. Calls one function.
    
**snip_l2_05_d.py**

    Define a function to get data from the User at the command line.
    Use while True loop to ensure data is entered or data is of the desired
    type.
    Apply format() function to the input() function.
    Use variables to hold text and prompt strings and pass them to the
    function.
    Simple program flow. One function.
    
**snip_l2_05_e.py**

    Define a function to get data from the User at the command line.
    Use 'while True' loop to ensure data is entered or data is of the desired
    type.
    Apply format() function to the input() function.
    Use variables to hold text and prompt strings and pass them to the
    function.
    Allow command line options to change prompt and text of input() function
    
**snip_l2_06_a.py**

    Define a function to get data from the User at the command line.
    Use 'while True' loop to ensure data is entered or data is of the desired
    type. i.e. Integer.
    Apply format() function to the input() function.
    Use variables to hold text and prompt strings and pass them to the
    function.
    Allow command line options to change prompt and text of input() function
    
**snip_l2_06_b.py**

    Define a function to get data from the User at the command line.
    Use 'while True' loop to ensure data is entered or data is of the desired
    type. i.e. Integer. If integer is negative return as positive. ie. abs()
    Apply format() function to the input() function.
    Use variables to hold text and prompt strings and pass them to the
    function.
    Allow command line options to change prompt and text of input() function.
    
**snip_l2_06_c.py**

    Define a function to get data from the User at the command line.
    Use 'while True' loop to ensure data is entered or data is of the desired
    type. Get integer, positive integer, float.
    Apply format() function to the input() function.
    A main() function is defined to call the other functions.
    
**snip_l2_06_d.py**

    Define a function to get data from the User at the command line.
    Use 'while True' loop to ensure data is entered or data is of the desired
    type. Get and integer, get any integer return a positive integer,
    or get integer or float and return a float.
    Apply format() function to the input() function.
    A main() function is defined to call the other functions.
    Enable debugging with -d or --debug commadn line option.
    Procedural programming style.
    
**snip_l2_07_a.py**

    Circle calculations. Enter the radius.
    Calculate circumference and area of the circle.
    Use 3.1415 within the calculations for value of Pi.
    Simple flow programming style.
    
**snip_l2_07_b.py**

    Circle calculations. Enter the radius.
    Calculate circumference and area of the circle.
    Use a constant of 3.1415 for PI.
    Simple flow programming style.
    
**snip_l2_07_c.py**

    Circle calculations. Enter the radius.
    Calculate circumference and area of the circle.
    Import math and use math.pi for the constant for PI.
    Simple flow programming.
    
**snip_l2_07_d.py**

    Circle calculations. Enter the radius.
    Calculate circumference and area of the circle.
    Use math.pi
    Call the float input function.
    No formatting of the calculated values
    Simple flow programming style. Only calls input of radius function.
    
**snip_l2_07_e.py**

    Circle calculations. Enter the radius.
    Use functions to calculate circumference and area of the circle.
    Use math.pi
    Use a float input function.
    No formatting of the calculated values.
    Simple flow programming, but calling 3 x functions.
    
**snip_l2_07_f.py**

    Circle calculations. Enter the radius.
    Use functions to calculate circumference and area of the circle.
    Use math.pi
    Use a float input function.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    
**snip_l2_07_g.py**

    Circle calculations. Enter the radius.
    Use one function to calculate circumference and area of the circle.
    Use math.pi
    Use a float input function.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Procedural programming style.
    
**snip_l2_08_a.py**

    Sphere calculations. Enter the radius.
    Calculate surface area and volume of a shpere.
    Use math.pi
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Sphere Formulas
    A = 4 Pi r**2
    V = 4/3 Pi r**3
    Simple flow programming style.
    
**snip_l2_08_b.py**

    Sphere calculations. Enter the radius.
    Calculate surface area and volume of a shpere.
    Use math.pi
    Use a float input function and functions to calculate surface area and
    volume.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Procedural programming style
    
**snip_l2_09_a.py**

    Cube calculations. Enter the length of an edge.
    Calculate surface area, volume and internal diagonal.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Cube algorithms
    surface = 6 * edge ^2
    volume = edge ^3
    diagonal through the space of the cube = square root 3 * edge
    Simple flow programming style
    
**snip_l2_09_b.py**

    Cube calculations. Enter the length of an edge.
    Calculate surface area, volume and internal diagonal using functions.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Procedural programming style.
    
**snip_l2_09_c.py**

    Cube calculations. Enter the length of an edge.
    Calculate surface area, volume and internal diagonal using one function.
    formats {:g} provides numeric rounding. E.g. 314.1592653589793 to  314.159.
    Procedural programming style.
    
**snip_l2_10_a.py**

    Get integer entry as radius. Use functions to calculate diameter,
    circumference and area of circle. Use iteration and output data each loop.
    
**snip_l2_10_b.py**

    Get integer entry as radius. Use functions to calculate diameter,
    circumference and area of circle. Use iteration and output data each loop.
    Procedural programming style.
    
**snip_l2_11_a.py**

    Get integer entry as radius. Calculate circumference, surface area and
    volume of sphere. Use iteration and output data each loop.
    Simple programming flow.
    
**snip_l2_11_b.py**

    Get integer entry as radius. Use functions to calculate circumference,
    surface area and volume of sphere. Use iteration and output data each loop.
    Procedural programming style.
    
**snip_l2_12_a.py**

    Get integer entry for cubic meters. Calculate radius, diameter, and
    circumference in meters, of sphere holding this volume.
    Use iteration and output data for each loop.
    Simple programming flow.
    
**snip_l2_12_b.py**

    Get integer entry for cubic meters. Use functions to calculate radius,
    diameter, and circumference in meters, of sphere holding this volume.
    Use iteration and output data for each loop.
    Procedural programming style.
    
**snip_l2_13_a.py**

    Get integer entry for litres. Calculate radius, diameter, and
    circumference in centimeters, of sphere holding this volume.
    Use iteration and output data for each loop.
    Simple programming flow.
    
**snip_l2_13_b.py**

    Get integer entry for litres. Use functions to calculate radius,
    diameter, and circumference in centimeters, of sphere holding this volume.
    Requires multiplying the radius formula by 10
    Use iteration and output data for each loop.
    Procedural programming style.
    
**snip_l2_14_a.py**

    Get integer entry as radius. Calculate diameter, circumference and area of
    circle. Use iteration and output data each loop.
    Output the data to a .csv file, suitable for reading into a spreadsheet
    Simple programming flow.
    
**snip_l2_14_b.py**

    Get integer entry as radius. Use functions to calculate diameter,
    circumference and area of circle. Use iteration and output data each loop.
    Generates the comma seperated value output file snip_l2_14_b.csv.
    Procedural programming style.
    
**snip_l2_14_c.py**

    Get integer entry as radius. Use functions to calculate diameter,
    circumference and area of circle. Use iteration and output data each loop.
    Calls function to generates the comma seperated value output file
    snip_l2_14_c.csv.
    Procedural programming style.
    
**snip_l2_15_a.py**

    Get integer entry as cube edge length. Calculate cube surface area, volume
    and the lenght of the internal diagonal. Use iteration and output data
    each loop.
    Output the data to a .csv file, suitable for reading into a spreadsheet
    
snip_l2_15_b.py**

    Get integer entry as cube edge length. Use functions to calculate cube
    surface area, volume and the lenght of the internal diagonal.
    Use iteration and output data each loop.
    Output the data to a .csv file, suitable for reading into a spreadsheet.
    
**snip_l2_15_c.py**

    Get integer entry as cube edge length. Use functions to calculate cube
    surface area, volume and the lenght of the internal diagonal.
    Use iteration and output data each loop.
    Output the data to a .csv file, suitable for reading into a spreadsheet.
    
**snip_l2_16_a.py**

    Produce the Fibonacci series. Get integer for how many in the series to
    produce. As these are integers, they are accurately produced to infinite.
    
**snip_l2_16_b.py**

    Produce the Fibonacci series. Get integer for how many in the series to
    produce. As these are integers, they are accurately produced to infinite.
    Enumerate the sequence and use commas in the numeric display.
    
**snip_l2_17_a.py**

    Demonstration of large integers and integer operators.
    Multiplication *, Exponent **, Addition +, and Modulus %
    
**snip_l2_17_b.py**

    Continuing demonstration of large integers and integer operators.
    Multiplication *, Exponent **, Addition +
    
**snip_l2_17_c.py**

    Continuing demonstration of large integers and integer operators.
    Addition +, Subtraction -, and Exponent **
    
**snip_l2_17_d.py**

    Continuing demonstration of large integers and integer operators.
    Integer Division //, and Modulo %
    
**snip_l2_18_a.py**

    Real scenario demonstration of large integers and integer operators.
    Addition +, Multiplicaton *, Integer Division //, Modulo %
    
**snip_l2_18_b.py**

    Introduce the float type. Multiplying by a floating point decimal.
    Addition +, Multiplication *
    
**snip_l2_19_a.py**

    Bicycle pedding cadence and sprocket ratios to determine speeds in each
    gear. Introduces list[] and for loop iterating over a list.
    Simple programming flow style.
    
**snip_l2_19_b.py**

    Bicycle pedding cadence and sprocket ratios to determine speeds in each
    gear using functions. Introduces list[] and for loop iterating over a list.
    Written in procedural programming style
    
**snip_l2_20_a.py**

    Floating point. Demonstration of adding 0.1
    
**snip_l2_20_b.py**

    Floating point. Demonstration of 1/10, while is equal to 0.1 in decimal
    is in binary 0.00011 and then infinately recurring 0011.
    
**snip_l2_20_c.py**

    Floating point. Demonstration Max positve value of float.
    
**snip_l2_21_a.py**

    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime
    int(math.sqrt(integer_under_test))
    
**snip_l2_21_b.py**

    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime
    int(math.sqrt(integer_under_test))
    Provide statistics and better listing.
    
**snip_l2_21_c.py**

    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime
    int(math.sqrt(integer_under_test))
    Provide heading and include count of number of modulo operations.
    Include the time taken to perform the calculations
    
**snip_l2_21_d.py**

    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime
    int(math.sqrt(integer_under_test))
    Provide heading with number of primes located
    Include the time taken to perform the calculations
    Procedural programming style.
    
**snip_l2_21_e.py**

    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime
    int(math.sqrt(integer_under_test))
    Provide heading with number of primes located.
    Include the time taken to perform the calculations.
    Include count of number of recursive modulo operations
    Procedural programming style.
    
**snip_l2_21_f.py**

    Locate prime numbers. Use recursive division up to the square root of
    the integer being tested for being a prime.
    int(math.sqrt(integer_under_test))
    Provide heading with number of primes located.
    Include the time taken to perform the calculations.
    Include count of number of recursive modulo operations
    Include Progress Bar
    Procedural programming style.
    
**snip_l2_22_a.py**

    Based on the length of an edge of a tetrahedron provide the dimensions.
    Tetrahedron a = edge
    Volume = a^3/(6 sqrt(2)
    Area = sqrt(3) a^2
    Face Area = (sqrt(3)/4) a^2
    Height = sqrt(2/3) a
    
**snip_l2_23_a.py**

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
    
**snip_l2_23_b.py**

    Demonstrate ANSI escape sequences for direct cursor addressing and setting
    forground and back ground colours on a console.
    Perform line drawing on a console using the box drawing character set.
    On Microsoft Windows console this is better than using the ANSI escape
    sequence box drawing as it is missing the ability to do the cross-hairs.
    Draw vertical bars of colour and indicates their numeric colour value.
    A draw_rectangle function has the arguments (x, y, width,height, foreground
    colour, background colour).
    Also sets the console windows title with ESC ] 2 ; <string> BEL
    
**snip_l2_23_c.py**

    Demonstrate ANSI escape sequences for direct cursor addressing and setting
    forground and back ground colours on a console.
    Perform line drawing on a console using the box drawing character set.
    On Microsoft Windows console this is better than using the ANSI escape
    sequence box drawing as it is missing the ability to do the cross-hairs.
    Draw reducing sized rectangles in different colours.
    Use print(EscapeSequence, end="", flush=True) to prevent newline character.
    Functions: draw_rectangle(), colour_check(), write_text()
    Also added COLOUR as a read-only dictionary to convert colour names to
    numeric string for the colour. If invalid colour data then remain with the
    default console colours.
    Sets the console windows title with ESC ] 2 ; <string> BEL
    
**snip_l2_23_d.py**

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
    
**snip_l2_23_e.py**

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
    
**snip_l2_24_a.py**

    Review the character set to determine if it includes the box drawing
    set of characters.
    
**snip_l2_24_b.py**

    Draw four styles of boxes from the Unicode Box Drawing set of characters.
    
**snip_l2_24_c.py**

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
    
**snip_l2_24_d.py**

    Making use of Direct Cursor addressing, and colour.
    Line Drawing is part of the ASCII character set.
    Does not require ANSI escape sequences to perform the drawing.
    Supported on Windows 10 patched to May 2016 revision or later.
    Uses methods for each line drawing graphic character. Uses double lines.

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
    

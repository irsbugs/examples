# Code Templates in Python - Level 2
Links: [Github](https://github.com/irsbugs/examples/blob/master/ncea_level2/templates/README.md) or [Website](https://irsbugs.github.io/examples/ncea_level2/templates/) 

These code templates may be useful for anyone who is learning the Python programming language. The templates use the procedural programming style. These templates are numbered and they are associated with the same numbered programs in the [snippets folder](https://github.com/HamPUG/examples/tree/master/ncea_level2/snippets). 

The top and bottom of these template programs remains much the same for each program. At the top of each program the template provides: shebang, importing modules, program description, copywrite, defining constants and variables. At the bottom of each program the template provides: `if __name__ == '__main__':`, help information function, python version check function, log file append function, command line argument parsing including debugging and help flags, and calls the main() function.

The middle section of these template programs is what changes to give each program its unique features. It contains a main() function which includes calls to other functions.

These template programs highlight the use of function code blocks, but do not utilise classes. They also assume the program is written as one file, and importing of modules is restricted to a small set of the builtin python modules. 

The programs are all console terminal based and there is no use of GUI windowing.

These templates were developed using Python 3.4. They have been tested on Ubuntu Linux and Windows10 desktop environments.

New Zealand secondary school teachers and students may find these template useful for the Digital Technologies, Level 2, Achievement Standards [91372](http://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2017/as91372.pdf) and [91373](http://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2017/as91373.pdf).

In a classroom computer lab that uses Windows10 desktop computers, the console terminal window applications (CMD and Powershell) may have been made unavailable on the students desktop computers. In the Windows10 file manager, if a *python* file is double-clicked it will launch a terminal window to run the python program. When the program completes, this terminal window is closed. To prevent the programs closing before a student has been able to see what the program does, all these snippet programs end with the lines...
   
    input("Press Enter key to end the program.")
    sys.exit()

Ian Stewart - 2016 © [![](https://licensebuttons.net/l/by/4.0/80x15.png)](https://creativecommons.org/licenses/by/4.0/)

## Template Programs

**template_l2_01.py** - *Fundament_Components*

Python program. Fundamental programming style components.
Includes: Shebang, encoding, Commented text in help(), 
Importing modules, variables, constants, python2 check, 
main function, cli help(), `if __name__ == '__main__':`, 
cli sys.argv list, debug, call main()

**template_l2_02.py** - *Time-Stamped_Logging*

Python program using a procedural programming style.
Add Logging of time-stamped data

**template_l2_03.py** - *Check_Python_Min_Version*

Python program using a procedural programming style.
Add: Check python is above the minimum version.

**template_l2_04.py** - *Functions*

Python program using a procedural programming style.
Add: 2 x functions. Includes data-type testing and +=1
Data can be passed as a command line option.

**template_l2_05.py** - *Input_From_Console*

Python program using a procedural programming style...
Get integer or floating point value from console.

**template_l2_06.py** - *Input_Integer_From_Console*

Python program using a procedural programming style...
Add: Integer only data from console.

**template_l2_07.py** - *Circle_Calculator*

When provided with the a value for the radius, the circle 
calculator program will determine the circles 
circumference and area.

**template_l2_08.py** - *Sphere_Calculator*

When provided with the a value for the radius, the sphere 
calculator program will determine the spheres 
surface area and volume.

**template_l2_09.py** - *Cube_Calculator*

When provided with the length of the edge of a cube 
calculator program will determine the cubes 
surface area, volume, and space diagonal.

**template_l2_10.py** - *Circle_Plotter*

When provided with a range of integer values for a radius
the circle plotter program will determine the
diameter, circumference and area.
The output may be cut and pasted into a spreadsheet.
If so, space delimiters must be merged.

**template_l2_11.py** - *Sphere_Plotter*

When provided with a range of integer values for a radius
the sphere plotter program will determine the
circumference, surface area and volume.
The output may be cut and pasted into a spreadsheet.
If so, space delimiters must be merged.

**template_l2_12.py** - *Sphere_Volume_Plotter*

When provided with a range of integer values for the
cubic meter volume of a sphere, the sphere volume plotter
program will determine the radius, diameter and 
circumference of the sphere in meters.
The output may be cut and pasted into a spreadsheet.
If so, space delimiters must be merged.

**template_l2_13.py** - *Sphere_Litre_Plotter*

When provided with a range of integer values for the
litres a sphere will hold, the sphere litre plotter
program will determine the radius, diameter and 
circumference of the sphere in centimeters.
The output may be cut and pasted into a spreadsheet.
If so, space delimiters must be merged.

**template_l2_14.py** - *Circle_Plotter_CSV*

When provided with a range of integer values for a radius
the circle plotter program will determine the
diameter, circumference and area. Like template_l2_10.py
The data is output to a comma seperated values (.csv) file.

**template_l2_15.py** - *Cube_Plotter_CSV*

When provided with the length of the edge of a cube 
calculator program will determine the cubes 
surface area, volume, and space diagonal.
Similar to template_l2_09.py
The data is output to a comma seperated values (.csv) file
The function update_data() is called from main().

**template_l2_16.py** - *Fibonacci_sequence*

Generate the Fibonacci sequence of integers.
The total for the sequence may be selected.
As each Fibonacci number in the sequence is generated 
it is appended to a list.
The items in the list are then output to the console.
The sequence has been limited to 200 so they are easier
to read on the console.
Highlights there is no limit to python integer arithmetic

**template_l2_17.py** - *Integer_Fun*

Demonstrate the arithmetic performed on integers is 
accurate and has no limits.
Starting with a funny number it is manipulated with
multiplication (*), addition (+) and exponents (**) to 
create an integer that is comprised of only one's.
Also highlights use of the modulo operator (%) and pythons
integer division (//), which is floor division.

**template_l2_18.py** - *Integer_Distance*

Demonstrate the arithmetic performed on integers is 
accurate and has no limits.
Introduce floating point calculation.

**template_l2_19.py** - *Bike_Speed*

Determine the speed of a bicycle. Parameters that may be
adjusted are:
1. Diameter of the rear wheel.
2. Cadence. The revolutions per minute of the pedalling.
3. Crankset teeth. Number of teeth on the front sprocket.
A list provides the number of teeth on each sprocket of
the casette on the rear wheel.
Input values are Integers. Calculations are mostly floats.

**template_l2_20.py** - *Floating_Point*

Demonstrate floating-point arithmetic and 
highlight some of its issues and limitations.

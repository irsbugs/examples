#!/usr/bin/env python3
#
# Program:      simple_calculator.py
#
# Objective:    NCEA example program
#               Uses the tkinter GUI
#
# Written for:  Hamilton Python User Group - Presentation 9 May 2016
#               https://github.com/hampug
#               http://www.meetup.com/nzpug-hamilton/
#
# Author:       Ian Stewart
#
# Date:         2016-Apr-24
#
# Copyright:    This work is licensed under a Creative Commons
#               Attribution-ShareAlike 4.0 International License.
#               http://creativecommons.org/licenses/by-sa/4.0/
#
# Notes:
# 1. Indentation method: 4 x space characters per indentation
#
# Python modules to be imported. Plus checking
import sys
from decimal import *

# Tested on Windows 7/10 Python 3.4.4 OK. 2016 - July 
# Check OS platform:
#if (sys.platform) == "linux" or (sys.platform) == "linux2":
#    # Program was developed on Linux so it should work OK.
#    pass
#else:
#    print("WARNING: This program was developed and tested on Linux.\n"
#          "It may need modifications for the Operating System you are using.")

# Check Python is version 3
if int(sys.version[0]) < 3:
    print("Python Version Error: Run program using python3 to support "
          "tkinter.\nExiting...")
    sys.exit()
# Import tkinter, ttk, and other tkinter modules
try:
    import tkinter as tk
except ImportError as e:
    print("Import Error: {}".format(e))
    print("tkinter module for python3 is not available.")
    print("To install tkinter: $ sudo apt-get install python3-tk")
    sys.exit(1)
try:
    from tkinter import ttk
except ImportError as e:
    print("Import Error: {}".format(e))
    print("Import Error: tkinter.ttk module is not available.")
    print("To install tkinter: $ sudo apt-get install python3-tk")
    sys.exit(1)
try:
    import tkinter.messagebox as tkmsgbox
except:
    print("tkinter does not include messagebox module")
    sys.exit(1)

TITLE_1 = "Simple Calculator"
FONT = ('FreeSans', 12, "normal")
# Position of digits on grid 0 to 9
DISPLAY_1_POSITION = ((0,0),)
DISPLAY_2_POSITION = ((1,0),)
DIGIT_POSITION = ((5,0),(4,2),(4,1),(4,0),(3,2),(3,1),(3,0),(2,2),(2,1),(2,0))
POINT_POSITION = ((5,1),)
MINUS_POSITION = ((5,2),)
DELETE_POSITION = ((3,4),)
DELETE_SYMBOL = "Delete"  # <-
CLEAR_POSITION = ((2,4),)
CLEAR_SYMBOL = "Clear"  # <<-
EQUAL_POSITION = ((4,4),)
OPERATOR_POSITION = ((2,3),(3,3),(4,3),(5,3))
OPERATOR_SYMBOLS = ("/", "*", "+", "-")
HELP_TITLE = "Simple Calculator"
HELP_TEXT = """Simple Calculator - Help
This simple calculator program uses the decimal module 
to perform accurate calculations. 
"""
MSGBOX_TITLE = "Simple Calculator - About..."
MSGBOX_TEXT = ("""Simple Calculator program.
An NCEA Example program.
Hamilton Python User Group.
https://github.com/hampug
Author: Ian Stewart
Date: 2016-04-24

This work is licensed under a Creative Commons
Attribution-ShareAlike 4.0 International License.
http://creativecommons.org/licenses/by-sa/4.0/
""")

class Calculator(ttk.Frame):
    """Calculator"""
    def __init__(self, parent):
        """Initilization"""
        ttk.Frame.__init__(self, parent)
        # print(dir(self))
        # print(dir(parent))
        self.master.title(TITLE_1)
        # Variables for Calculator class
        self.parent = parent
        self.num = ["",""]
        self.display = ""
        self.operator = ""
        self.result = ""
        # Position index of a number in the equation.
        self.numidx = 0
        # Setup 
        self.create_widgets()
        #self.action_on_launch()

    def create_widgets(self):
        """Setup the widgets"""
        # ===== Create styles for use with ttk widgets =====
        self.style = ttk.Style()
        # Change a root style to modify all widgets.
        self.style.configure('.', font=(FONT))


        # The buttons do not need to be kept in a list
        self.button_list = []

        # Create the buttons for digits 0 to 9
        for i in range(10):
            button = ttk.Button(self, text=str(i),
                                command=lambda i = str(i): 
                                self.digit_callback(i))
            button.grid(row=DIGIT_POSITION[i][0], 
                        column=DIGIT_POSITION[i][1], padx=1, pady=1)    
            #self.button_list.append(button)

        # Create decimal point button
        i = "."
        button = ttk.Button(self, text=str(i),
                            command=lambda i = i: 
                            self.decimal_point_callback(i))
        button.grid(row=POINT_POSITION[0][0], 
                    column=POINT_POSITION[0][1], padx=1, pady=1)
        #self.button_list.append(button)

        # Create plus / minus toggle of the number
        i = "+/-"
        button = ttk.Button(self, text=str(i),
                            command=lambda i = i: 
                            self.minus_callback(i))
        button.grid(row=MINUS_POSITION[0][0], 
                    column=MINUS_POSITION[0][1], padx=1, pady=1)
        #self.button_list.append(button)
        # Create the operators + - * /
        #for i in range(4):
        for i,j in enumerate(OPERATOR_SYMBOLS):
            button = ttk.Button(self, text=str(j),
                                command=lambda j = str(j): 
                                self.operator_callback(j))
            button.grid(row=OPERATOR_POSITION[i][0], 
                        column=OPERATOR_POSITION[i][1], padx=1, pady=1)    
            #self.button_list.append(button)

        # Button to delete last entered character
        i = DELETE_SYMBOL
        button = ttk.Button(self, text=str(i),
                            command=lambda i = i: 
                            self.delete_callback())
        button.grid(row=DELETE_POSITION[0][0], 
                    column=DELETE_POSITION[0][1], padx=1, pady=1)
        #self.button_list.append(button)

        # Button to clear all data - reset
        i = CLEAR_SYMBOL
        button = ttk.Button(self, text=str(i),
                            command=lambda i = i: 
                            self.delete_all_callback())
        button.grid(row=CLEAR_POSITION[0][0], 
                    column=CLEAR_POSITION[0][1], padx=1, pady=1)
        #self.button_list.append(button)

        # Button to calculate the equation.
        i = "="
        button = ttk.Button(self, text=str(i),
                            command=lambda i = i: 
                            self.equal_callback())
        button.grid(row=EQUAL_POSITION[0][0], 
                    column=EQUAL_POSITION[0][1], 
                    rowspan=2, padx=1, pady=1, sticky="ns")
        #self.button_list.append(button)

        # Label for equation
        self.display_1 = ttk.Label(self, text="") #, wraplength=500)
        self.display_1.grid(row=DISPLAY_1_POSITION[0][0], 
                          column=DISPLAY_1_POSITION[0][1], 
                          padx=5, pady=1, columnspan=5, sticky="e")
        # Label for result
        self.display_2 = ttk.Label(self, text="")
        self.display_2.grid(row=DISPLAY_2_POSITION[0][0], 
                          column=DISPLAY_2_POSITION[0][1], 
                          padx=5, pady=1, columnspan=5, sticky="e")

        # Provide a menubar
        self.printout = tk.BooleanVar()
        #self.printout = False

        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)
        self.filemenu = tk.Menu(menubar, tearoff=False, font=FONT)
        # Checkbox to turn on/off output to the console 
        self.filemenu.add_checkbutton(label="Output calculations", onvalue=True, 
                                      offvalue=False, variable=self.printout)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.menu_exit)
        menubar.add_cascade(label="File", menu=self.filemenu, font=FONT)
        self.helpmenu = tk.Menu(menubar, tearoff=False, font=FONT)
        self.helpmenu.add_command(label="Help", command=self.menu_help)
        self.helpmenu.add_command(label="About...", command=self.menu_about)
        menubar.add_cascade(label="Help", menu=self.helpmenu, font=FONT)

        # This will disable the item at index 0 on the File menu. i.e. "Save"
        #self.filemenu.entryconfig(0, state=tk.DISABLED)

    # =========================================================================
    def menu_exit(self):
        """"""
        sys.exit(1)

    def menu_help(self):
        """"""
        tkmsgbox.showinfo(HELP_TITLE, HELP_TEXT)
        pass

    def menu_about(self):
        """Menubar. Messsage box to display the About info"""
        tkmsgbox.showinfo(MSGBOX_TITLE, MSGBOX_TEXT)

    def operator_callback(self, string):
        """
        The first number has been entered now add the operator
        If second number has been entered then calculate and display, and move
        result to first number to be ready to continue with equation.        
        """
        # If first number not present ignore
        if not self.num[0]:
            return

        # If first number ends in a decimal point strip decimal point.
        if self.num[0][-1] == ".":
            self.num[0] = self.num[0][:-1]
        # If second number exists, call execution of equation, which stores 
        # result as num[0]. Then add the operator
        if self.num[1]:
            if self.operator:
                self.calculate_equation()                

        # Number index goes to 1 to load next number into self.num[1]
        self.numidx = 1
        # Update the operator 
        self.operator = string
        # Display equation
        self.display_1.config(text="{} {} {}"
                              .format(self.num[0], self.operator, self.num[1]))
        # Clear the result
        self.display_2.config(text="")

    def equal_callback(self):
        """Calculate the equation"""
        # If second number not entered then don't calculate
        if not self.num[1]:
            return
        self.calculate_equation()
        # After and ='s then clear all data for a fresh start.
        self.num[0] = ""
        self.num[1] = ""
        self.operator = ""
        self.numidx = 0
        self.result = ""

    def calculate_equation(self):
        """
        Calculate the Equation. num[0] and num[1] exist. 
        Use self.operator to calculate the result.
        Pass the result to self.num[0] to allow continued calculations. 
        Note: Decimal arithmetic is used rather than float. 
        Decimals must be passed strings       
        """
        # if num1 ends in a . then strip it.
        if self.num[1][-1] == ".":
            self.num[1] = self.num[1][:-1]

        if self.operator == "/":
            # Avoid divide by zero. Don't proceed with calculation
            if float(self.num[1]) == 0.0:
                print("Blocked: Attempt to divide by zero")
                return     
            answer = Decimal(self.num[0]) / Decimal(self.num[1])
            
        if self.operator == "*":
            answer = Decimal(self.num[0]) * Decimal(self.num[1])       

        if self.operator == "+":
            answer = Decimal(self.num[0]) + Decimal(self.num[1])      

        if self.operator == "-":
            answer = Decimal(self.num[0]) - Decimal(self.num[1])
            
        self.result = str(answer)
        # decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]

        # Display equation
        self.display_1.config(text="{} {} {} = "
                              .format(self.num[0], self.operator, self.num[1]))
        # Display result
        self.display_2.config(text="{}".format(self.result))

        #print(self.printout.get())
        # Output to console
        if self.printout.get():   
            print("{} {} {} = {}".format(
                  self.num[0], self.operator, self.num[1], self.result))

        # Update the first number as the result to continue the calculations
        # Convert result to a string so self.num[0] remains a string
        self.num[0] = self.result
        self.num[1] = ""
        self.operator = ""
        # Point to second number. Only change back to 0 on a clear
        self.numidx = 1

    def delete_all_callback(self):
        """Delete all of both numeric strings"""
        self.num = ["",""]
        self.operator = ""
        # Clear both display labels
        self.display_1.config(text="")
        self.display_2.config(text="")

        # Set number index so next number goes into self.num[0]
        self.numidx = 0


    def delete_callback(self):
        """Delete from right hand side of number"""
        if len(self.num[self.numidx]) == 0:
            return
        self.num[self.numidx] = self.num[self.numidx][0:-1]

        # Display equation
        self.display_1.config(text="{} {} {}"
                              .format(self.num[0], self.operator, self.num[1]))        

    def minus_callback(self, string):
        """Toggle a minus sign at the beginning of the number"""
        # If number is 0, then don't toggle + / - 
        # Do not allow adding +/- if empty, 0, or 0. 
        if len(self.num[self.numidx]) == 0:
            return
        if self.num[self.numidx] == "0":
            return
        if self.num[self.numidx] == "0.":
            return
        # Strip off or add -
        if self.num[self.numidx][0] == "-":
            # Strip off minus
            self.num[self.numidx] = self.num[self.numidx][1:]
        else:
            # place minus at the front
            self.num[self.numidx] = "-" + self.num[self.numidx]

        # Display equation
        self.display_1.config(text="{} {} {}"
                              .format(self.num[0], self.operator, self.num[1]))          

    def decimal_point_callback(self,string):
        """Append Decimal point to the number string."""
        # Ignore decimal place if it already exists.
        if "." in self.num[self.numidx]:
            return
        # Prevent building second number if self.operator not defined
        if self.numidx == 1:
            if not self.operator:
                return

        # Place a leading 0 in front of decimal point if its first in string.
        if len(self.num[self.numidx]) == 0:
            self.num[self.numidx] = "0"

        # Add the decimal point.
        self.num[self.numidx] = self.num[self.numidx] + string

        # Display equation
        self.display_1.config(text="{} {} {}"
                              .format(self.num[0], self.operator, self.num[1]))

    def digit_callback(self, string):
        """Digit 0 to 9 buttons. Build the number"""
        # Prevent building second number if self.operator not defined
        if self.numidx == 1:
            if not self.operator:
                return
        # Concatinate to build the number
        self.num[self.numidx] = self.num[self.numidx] + string
        # If number started with 0. Remove the 0.
        if len(self.num[self.numidx]) == 2:
            if self.num[self.numidx][0] == "0":
                self.num[self.numidx] = self.num[self.numidx][1]

        # Display equation
        self.display_1.config(text="{} {} {}"
                              .format(self.num[0], self.operator, self.num[1]))

        # Clear the result
        self.display_2.config(text="")


if __name__ == "__main__":
    """Check for command line arguments."""
    print(TITLE_1)
    # Check for help
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print(HELP)
            sys.exit(1)

    # Launch tkinter GUI.
    root = tk.Tk()

    # Position the GUI on the display screen. +pixels x-axis + pixels y-axis
    root.geometry('+100+50')
    # Open the GUI Calculator class. Use grid to allow future expansion.
    main_gui = (Calculator(root).grid(row=0, column=0, sticky="we"))

    root.mainloop()

'''
Notes: The decimal module is used to do accurate mathematics:
Normal floating point mathematics...
>>> 1.1 + 1.1
2.2
>>> 1.1 + 1.2
2.3
>>> 1.1 + 1.3
2.4000000000000004

Using decimal.Decimal() function to add 1.1 to 1.3...
from decimal import *

>>> Decimal(1.1) + Decimal(1.3)
Decimal('2.400000000000000133226762955')

Note: Decimal should be supplied a string...
>>> Decimal("1.1") + Decimal("1.3")
Decimal('2.4')

OR...
>>> str(Decimal("1.1") + Decimal("1.3"))
'2.4'
>>> 

Suggestion: import operator
From dir(operator)...
abs, add, and_, attrgetter, concat, contains, countOf, delitem, eq, floordiv, 
ge, getitem, gt, iadd, iand, iconcat, ifloordiv, ilshift, imod, imul, index, 
indexOf, inv, invert, ior, ipow, irshift, is_, is_not, isub, itemgetter, 
itruediv, ixor, le, length_hint, lshift, lt, methodcaller, mod, mul, ne, neg, 
not_, or_, pos, pow, rshift, setitem, sub, truediv, truth, xor

'''

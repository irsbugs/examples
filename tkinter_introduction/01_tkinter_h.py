#!/usr/bin/env python3
#
import tkinter
print("Instantiating the Window so attributes can be set and widgets added.")
main_window = tkinter.Tk()
main_window.geometry("300x50")
main_window.title("Hello")
main_window.configure(background="yellow")

# Add a label and a button to the main_window.
label = tkinter.Label(main_window, text="Hello World Label")
label.pack()
button = tkinter.Button(main_window, text="Button")
button.pack()

# Maintain the displaying of the window
main_window.mainloop()
"""
Instantiate the tkinter.Tk() window as the object "main_window".
Set attributes of geometry, title, background colour,  of main_window.
Add to main_window a label and a button. The button has no functionality.

To add functionality to the button so it will execute a routine when clicked
the "command=button_clicked_function" needs to be added to the program.

This may also be performed in an interactive python session...
>>> import tkinter
>>> main_window = tkinter.Tk()
>>> main_window.geometry("300x50")
''
>>> main_window.title("Hello World")
''
>>> label = tkinter.Label(main_window, text="Hello World Label")
>>> label.pack()
>>> button = tkinter.Button(main_window, text="Button")
>>> button.pack()
>>>

Author: Ian Stewart.
Date: 2016 July
This script is licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

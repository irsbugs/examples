#!/usr/bin/env python3
#
print("The window creation has been appended to include a title for the window")
import tkinter
tkinter.Tk().title("Hello")

# Add the following delay mechanism, so the Tk Window can be observed...
input("Hit Return key to exit")

"""
The tkinter.Tk() to launch a window is appended with the code to add a title
to the Window.

print(type(tkinter.Tk())) #  <class 'tkinter.Tk'>
print(type(tkinter.Tk().title("Hello"))) #  <class 'str'>

Author: Ian Stewart.
Date: 2016 July
This script is licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

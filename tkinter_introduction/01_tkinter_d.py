#!/usr/bin/env python3
#
print("The window creation has been appended to configure a red background")
import tkinter
tkinter.Tk().configure(background="red")

# Add the following delay mechanism, so the Tk Window can be observed...
input("Hit Return key to exit")

"""
The tkinter.Tk() to launch a window is appended with the code configure the
backgournd of the Window to be a red colour.

Note: Obtaining other key words to the configure() function:
>>> print(tkinter.Tk().configure().keys())
dict_keys(['screen', 'relief', 'height', 'background', 'padx', 'class',
'pady', 'bg', 'use', 'menu', 'takefocus', 'container', 'highlightbackground',
'highlightcolor', 'borderwidth', 'highlightthickness', 'bd', 'cursor',
'width', 'visual', 'colormap'])

Author: Ian Stewart.
Date: 2016 July
This script is licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

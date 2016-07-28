#!/usr/bin/env python3
#
import tkinter
import time
print("Using a timer to maintain displaying of the Window for 5 seconds")

# Use .update() to force window creation before sleep(5)
tkinter.Tk().update()

# Alternative delay mechanism. Provide 5 seconds of displaying the Window
time.sleep(5)

"""
Using a timer to maintain displaying the Window

tkinter.Tk() needs to be appended with the function update().
update() forces the Window to be displayed before the 5 seconds of sleeping
begins.

Note: As well as...
tkinter.Tk().update()
there is also...
tkinter.Tk().update_idletasks()


Author: Ian Stewart.
Date: 2016 July
This script is licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

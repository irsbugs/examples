#!/usr/bin/env python3
#
import tkinter
print("The geometry() function to modify the Windows dimensions and position.")
# Use tkinters Tk()
tkinter.Tk().geometry("400x100+200+500")

tkinter.mainloop()

"""
Set the Windows geometry. Values are in pixels.
Note: There can be no spaces in the string. E.g.
.geometry("400x500") <-- is OK
.geometry("400 x 500") <-- will fail.

Accepts just the dimensions, or may include the position on the desktop. E.g.
geometry("Width x Height")
OR
geometry("Width x Height + PositionX on Desktop + Position Y on Desktop")

Author: Ian Stewart.
Date: 2016 July
This script is licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

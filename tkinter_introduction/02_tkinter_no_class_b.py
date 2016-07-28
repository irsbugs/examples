#!/usr/bin/env python3
#
print("Tkinter Window without using a class. Uses StringVar and textvariable")
from tkinter import *
from tkinter import ttk

def on_button_1_click():
    """Change the labels text to 'hello'"""
    message.set("hello")

def on_button_2_click():
    """clear the labels text"""
    message.set("")

# Instantitate tkinter.Tk() as the object "root" 
root = Tk()
root.title("Hello")
# Instantiate the Windows frame as "mainframe" so widgets can be added
mainframe = ttk.Frame(root, padding="5 5 10 10")
mainframe.pack()

# Create message as a tkinter toolkit string variable.
message = StringVar()
message.set("Press a button")

# Create the widgets.
# The label connects textvariable to the string variable "message" 
ttk.Label(mainframe, textvariable=message).pack()
ttk.Button(mainframe, text="Hello", command=on_button_1_click).pack()
ttk.Button(mainframe, text="Clear", command=on_button_2_click).pack()

# Add some padding to the widgets
for child in mainframe.winfo_children(): 
    child.pack_configure(padx=50, pady=5)

root.mainloop()

"""
Use tkinter without creating a class,
Instantiate message = StringVar()
Set label to have the textvariable = message
When the buttons are clicked, then message.set("text")

Also loop through the children of mainframe (label, and 2 x buttons) and apply
padding from the edges of the frame.


Author: Ian Stewart.
Date: 2016 July
Scripts are licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

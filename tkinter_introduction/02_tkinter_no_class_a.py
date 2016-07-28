#!/usr/bin/env python3
#
print("Tkinter Window without using a class. Uses looping to find widgets")
from tkinter import Tk as tk
from tkinter import ttk

def button_1_click():
    """Button to enter 'hello' in widget named label1."""
    #print(len(mainframe.winfo_children())) #3 label and 2 x buttons
    for child in mainframe.winfo_children(): 
        if child.winfo_name() == "label1":
            child.configure(text="hello")        

def button_2_click():
    """Button to clear the contents of the widget named label1."""
    for child in mainframe.winfo_children(): 
        if child.winfo_name() == "label1":
            child.configure(text="") 

# Instantiate tkinter.Tk() as the object "root".    
root = tk()
root.title("Hello")
# Instantiate the Windows frame as "mainframe" so widgets can be added
mainframe = ttk.Frame(root)
mainframe.pack()

# Add widgets. A label and two buttons
ttk.Label(mainframe, 
          text="Press a button", 
          name="label1",
          font="FreeSans, 14").pack(pady=10)
ttk.Button(mainframe, text="Hello", command=button_1_click).pack(padx=50)
ttk.Button(mainframe, text="Clear", command=button_2_click).pack(padx=50)

# For additional padding of widgets from their frame borders
#for child in mainframe.winfo_children(): 
#    child.pack_configure(padx=30, pady=5)

# Maintain the displaying to the window
root.mainloop()

"""
Use tkinter without creating a class, and without instantiating the label
or the two buttons.

Requires looping through the children of instantiated mainframe to find
"label1", then use of the configure() function to a change to the text on the
label.

from tkinter import ttk
This allows using the themed toolkit widgets "ttk". The style, colour, fonts,
etc. of themed widgets is easier to make modifications to than the original
set of widgets.

Author: Ian Stewart.
Date: 2016 July
Scripts are licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

#!/usr/bin/env python3
#
print("Tkinter window using the class construct")
from tkinter import *
from tkinter import ttk

class MainWindow(ttk.Frame):
    """Create the Window with a label and two buttons"""
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Hello World")

        self.label = ttk.Label(self, text="Click a button")
        self.button_1 = ttk.Button(self, text="Hello", command=self.on_click_1)
        self.button_2 = ttk.Button(self, text="Clear", command=self.on_click_2)

        self.label.pack()
        self.button_1.pack()
        self.button_2.pack()
        self.pack()
        
    def on_click_1(self):
        """Set label to hello"""
        self.label.configure(text="hello")
        print("Hello button clicked")
        
    def on_click_2(self):
        """Clear the label"""
        self.label.configure(text="")
        print("Clear button clicked")
        
if __name__ == "__main__":
    root = Tk()
    root.geometry("250x100+200+200")
    application = MainWindow(root)
    root.mainloop()
    
"""
Simple use of tkinter using a class() construct.



Author: Ian Stewart.
Date: 2016 July
This script is licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

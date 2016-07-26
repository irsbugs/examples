#!/usr/bin/env python3
#
from tkinter import *
from tkinter import ttk

class MainWindow(ttk.Frame):
    """Create the main window"""
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Fibonacci series")

        self.label = ttk.Label(self, text="")
        self.button_1 = ttk.Button(self, text="Fibonacci series",
                                   command=self.on_click_1)
        self.button_2 = ttk.Button(self, text="Clear",
                                   command=self.on_click_2)

        self.label.pack()
        self.button_1.pack()
        self.button_2.pack()
        self.pack()

        self.fibonacci_list = [0,1]
        
    def on_click_1(self):
        for i in range(1, 15):
            self.fibonacci_list.append(self.fibonacci_list[i-1] +
                                       self.fibonacci_list[i])
        self.label.configure(text=self.fibonacci_list)
        self.fibonacci_list = [0,1]
        print("Debug Message: Button 1 clicked")
        
    def on_click_2(self):
        self.label.configure(text="")
        self.fibonacci_list = [0,1]
        print("Debug Message: Button 2 clicked")
        
if __name__ == "__main__":
    print("Starting Fibonacci python program")
    root = Tk()
    root.geometry("350x100+200+200")
    application = MainWindow(root)
    root.mainloop()
    
"""
Fibonacci series - tkinter. Has .py extension, so it opens a console window.

Fibonacci series with .py extension - This will launch the tkinter GUI as well
as a console window. The "debug" information will be printed to the console
window.

Author: Ian Stewart.
Date: 2016 July
This script is licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""
    

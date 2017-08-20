#!/usr/bin/env python3
#
# gtk_step_1.py
#
# Steps:
# 1. Create an empty window, with a title. Clicking on the X icon will close
#       the window and halt the program.
#
# Ian Stewart. Hamilton Python User Group. CC0. 20 August 2017
#
# Importing
import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Constants
TITLE = "Gtk - Step 1"


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=TITLE)


if __name__ == "__main__":
    print("Gtk Program started")

    window = MainWindow()  # <--- Instantiate the class
    window.connect("delete-event", Gtk.main_quit)  # <--- Allow process to end
    window.show_all()
    Gtk.main()  # <--- loop
    sys.exit("Gtk Program finished")

'''
Links:

https://python-gtk-3-tutorial.readthedocs.io/en/latest/

https://stackoverflow.com/questions/40074977/how-to-format-the-entries-in-gtk-entry/40163816
'''

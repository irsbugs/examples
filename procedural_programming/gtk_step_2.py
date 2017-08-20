#!/usr/bin/env python3
#
# gtk_step_2.py
#
# Steps:
# 1. Create an empty window, with a title. Clicking on the X icon will close
#       the window and halt the program.
# 2. Default Window size. Create main grid and add three frames.
#
# Ian Stewart. Hamilton Python User Group. CC0. 20 August 2017

# Importing
import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
#
# Constants
TITLE = "Gtk - Step 2"
F1_LABEL = "Frame 1"
F2_LABEL = "Frame 2"
F3_LABEL = "Frame 3"


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=TITLE)
        self.set_default_size(400, 200)

        # Create the main grid
        grid_main = Gtk.Grid()
        self.add(grid_main)

        # Insert three frames in the main grid.
        frame_1 = Gtk.Frame(margin=10)
        frame_1.set_label(F1_LABEL)
        grid_main.attach(frame_1, 0, 0, 1, 1)

        frame_2 = Gtk.Frame(margin=10)
        frame_2.set_label(F2_LABEL)
        grid_main.attach(frame_2, 0, 1, 1, 1)

        frame_3 = Gtk.Frame(margin=10)
        frame_3.set_label(F3_LABEL)
        grid_main.attach(frame_3, 0, 2, 1, 1)


if __name__ == "__main__":
    print("Gtk Program started")

    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
    sys.exit("Gtk Program finished")

'''
Links:

https://python-gtk-3-tutorial.readthedocs.io/en/latest/

https://stackoverflow.com/questions/40074977/how-to-format-the-entries-in-gtk-entry/40163816
'''

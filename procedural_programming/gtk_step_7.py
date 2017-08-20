#!/usr/bin/env python3
#
# gtk_step_7.py
#
# Steps:
# 1. Create an empty window, with a title. Clicking on the X icon will close
#       the window and halt the program.
# 2. Default Window size. Create main grid and add three frames.
# 3. Add a grid to each frame. Add a label to each frame.
# 4. Add an Entry widget in frame 1.
# 5. Import math. Calculate the circumference and the area based on Entry data.
# 6. Setup the labelling.
# 7. Use argpase to pass the radius via the command line. E.g. Launch program:
#       $ python3 gtk_step_7.py --radius 12.5
#
# Ian Stewart. Hamilton Python User Group. CC0. 20 August 2017
#
# Importing
import sys
import math
import argparse
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Constants and variables.
TITLE = "Circle Calculator - Step 7"
F1_LABEL = "Enter Radius"
F2_LABEL = "Circle Circumference"
F3_LABEL = "Circle Area"
F1_LABEL_1 = "Type 'Enter' key to calculate"
F2_LABEL_1 = ""
F3_LABEL_1 = ""
radius = 1

# Instantiate
parser = argparse.ArgumentParser(description=TITLE)


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=TITLE)
        # self.set_default_size(400, 200)
        # print(radius)

        # Create the main grid.
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

        # Create a grid in each frame.
        f1_grid = Gtk.Grid()
        frame_1.add(f1_grid)

        f2_grid = Gtk.Grid()
        frame_2.add(f2_grid)

        f3_grid = Gtk.Grid()
        frame_3.add(f3_grid)

        # Add label in each frame grid.
        self.f1_label_1 = Gtk.Label(margin=10)
        self.f1_label_1.set_text(F1_LABEL_1)
        f1_grid.attach(self.f1_label_1, 0, 0, 1, 1)

        self.f2_label_1 = Gtk.Label(margin=10)
        self.f2_label_1.set_text(F2_LABEL_1)
        f2_grid.attach(self.f2_label_1, 0, 0, 1, 1)

        self.f3_label_1 = Gtk.Label(margin=10)
        self.f3_label_1.set_text(F3_LABEL_1)
        f3_grid.attach(self.f3_label_1, 0, 0, 1, 1)

        # Add an entry field in Frame 1.
        self.f1_entry_1 = Gtk.Entry(margin=10)
        # self.f1_entry_1.set_text("1234567890")
        # "activate" is a callback for when the return key is typed after
        # entering the data into the Entry widget field.
        # Other entry callbacks include: "insert_text", and "changed".
        self.f1_entry_1.connect("activate", self.cb_f1_entry_1_activate)
        self.f1_entry_1.set_text("{}".format(radius))
        f1_grid.attach(self.f1_entry_1, 0, 1, 1, 1)

    def cb_f1_entry_1_activate(self, entry):
        """
        Entry Widget. Get here upon typing the enter key in the Entry widget.
        Try converting Entry text string to a float.
        If a float, then calculate the circle circumference and area.
        """
        # print("Entry widget contains:", entry.get_text())
        # Test if entry string is a float.
        try:
            radius = float(entry.get_text())
            # print("Entry widget string converts to floating point value: {}"
            #      .format(radius))
            self.f1_entry_1.set_text(str(radius))
            # Call methods to calculate circumference and area and then display
            circumference_string = self.calculate_circumference(radius)
            self.f2_label_1.set_text(circumference_string)
            area_string = self.calculate_area(radius)
            self.f3_label_1.set_text(self.calculate_area(radius))

        except ValueError:
            print("Entry widget string does not convert to float value.")
            self.f2_label_1.set_text("")
            self.f3_label_1.set_text("")

    def calculate_circumference(self, radius):
        """Use radius to calculate the circumference."""
        circumference = 2 * math.pi * radius
        return "{:g}".format(circumference)

    def calculate_area(self, radius):
        """Use radius to calculate the area."""
        area = math.pi * radius ** 2
        return "{:g}".format(area)


if __name__ == "__main__":
    print("Gtk Program started")
    # Use argparse to support --debug flag.
    parser.add_argument('-r', '--radius',
                        type=float,
                        help='Provide the prompting value for the radius.')
    # Instantiate
    args = parser.parse_args()
    # print(args)
    # Call the main function to control the program.
    if args.radius is not None:
        radius = args.radius

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

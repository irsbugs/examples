#!/usr/bin/env python3
#
# gtk_step_4_insert.py
#
# Steps:
# 1. Create an empty window, with a title. Clicking on the X icon will close
#       the window and halt the program.
# 2. Default Window size. Create main grid and add three frames.
# 3. Add a grid to each frame. Add a label to each frame.
# 4. Add an Entry widget in frame 1.
# Insert. The Entry widget also supports the callback based on "insert_text".
#       This allow checking of the text entered, such that an integer or float
#       is all that is acceptable input. It also allow some short-cut features,
#       for example, starting data entry with a decimal point, will
#       automatically be prefixed with a zero.
#
# Ian Stewart. Hamilton Python User Group. CC0. 20 August 2017
#
# Importing
import sys
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject
#
# Constants
TITLE = "Gtk - Step 4 - insert"
F1_LABEL = "Frame 1"
F2_LABEL = "Frame 2"
F3_LABEL = "Frame 3"

F1_LABEL_1 = "Frame 1 Label 1"
F2_LABEL_1 = "Frame 2 Label 1"
F3_LABEL_1 = "Frame 3 Label 1"


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=TITLE)
        self.set_default_size(250, 200)

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

        # Add an entry field in Frame 1. Changed is for each character entered.
        self.f1_entry_1 = Gtk.Entry(margin=10)
        # self.f1_entry_1.set_text("1234567890")
        # self.f1_entry_1.connect("changed", self.cb_f1_entry_1_changed)

        # Insert a float which can be negative.
        self.f1_entry_1.connect("insert_text", self.cb_f1_entry_1_insert_float)
        # Activate is when the return key is typed after entering the value.
        self.f1_entry_1.connect("activate", self.cb_f1_entry_1_activate)
        f1_grid.attach(self.f1_entry_1, 0, 1, 1, 1)

    def cb_f1_entry_1_insert_float(self, entry, text, length, position):
        """
        An entry widget that only allows positive and negative floating point
        values to be entered.
        The text is verified before it is entered into the entry field.
        While this callback has a "position" value it is always 0 due to a bug.
        Position of the cursor is achieved with: entry.get_position()
        Moving the position of the cursor requires:
        GObject.idle_add(entry.set_position, new_pos)
        """
        # print("Got to insert callback")
        pos = entry.get_position()
        old_text = entry.get_text()
        # print("Text_old:", old_text, "Text:", text, "Position:", pos)

        new_text = ""

        # Support limited pasting of multiple characters using float().
        # If text > 1 and old_text == "" i.e. pos zero, and text must
        # convert to a float.
        # If value is an integer, then strip the added .0 for a float.
        # .1 becomes 0.1, -.1 ==> -0.1, +.1 ==> 0.1, -123 ==> -123 not -123.0
        if len(text) > 1:
            if old_text == "":
                try:
                    value = float(text)
                    new_text = str(value)
                    # If integer, display string without the trailing .0
                    if value.is_integer():
                        new_text = new_text[:-2]
                    pos = len(new_text)
                    self.perform_insert(entry, new_text, pos)
                    return
                except ValueError:
                    # Doesn't convert to float so proceed no further.
                    self.perform_insert(entry, old_text, pos)
                    return
            else:
                # Don't append multi-character string to existing text.
                self.perform_insert(entry, old_text, pos)
                return

        # From here onward text validation is only one character of text.
        # Validate text - 1.
        # Only support these characters -.0123456789
        # Tested OK.
        if text not in "-.0123456789":
            # Do nothing.
            self.perform_insert(entry, old_text, pos)
            return

        # Insert minus sign. Can only be at position 0
        # Tested OK.
        if "-" not in old_text and text == "-" and pos == 0:
            self.perform_insert(entry, text + old_text, pos + 1)
            return

        # All "-" scenario's have been processed. Reject any more.
        # E.g. Old text already has a decimal point.
        if text == "-":
            # Do nothing.
            self.perform_insert(entry, old_text, pos)
            return

        # Insert the 0 as prefix for a decimal
        if text == "0" and pos == 0:
            if len(old_text) > 0:
                if "0" != old_text[0]:
                    text = "0."
                    # print(text + old_text)
                    self.perform_insert(entry, text + old_text, pos + 2)
                    return

                else:
                    # Do nothing.
                    self.perform_insert(entry, old_text, pos)
                    return
            else:
                text = "0."
                # print(text + old_text)
                self.perform_insert(entry, text + old_text, pos + 2)
                return

        # Insert the 0 as prefix for a minus decimal
        if text == "0" and pos == 1:
            if len(old_text) > 0:
                if "0" != old_text[0]:
                    text = "0."
                    # print(text + old_text)
                    pre_text = old_text[:pos]
                    post_text = old_text[pos:]
                    # print(pre_text, post_text)
                    new_text = pre_text + text + post_text
                    new_pos = pos + len(text)
                    self.perform_insert(entry, new_text, new_pos)
                    return

                else:
                    # Do nothing.
                    self.perform_insert(entry, old_text, pos)
                    return
            else:
                pass

        # If decimal is deleted don't allow adding more zeros
        if text == "0" and pos == 1:
            if len(old_text) > 0:
                if old_text[0] == "0":
                    # Do nothing.
                    self.perform_insert(entry, old_text, pos)
                    return

        # If decimal is deleted and minus don't allow adding more zeros
        if text == "0" and pos == 2:
            if len(old_text) > 1:
                if old_text[0:2] == "-0":
                    # Do nothing.
                    self.perform_insert(entry, old_text, pos)
                    return

        if text == "0" and pos > 1:
            # Normal insertion of a zero
            # print(text + old_text)
            pre_text = old_text[:pos]
            post_text = old_text[pos:]
            # print(pre_text, post_text)
            new_text = pre_text + text + post_text
            new_pos = pos + len(text)
            self.perform_insert(entry, new_text, new_pos)
            return

        if text == "." and pos == 0:
            if "." not in old_text:
                text = "0."
                # print(text + old_text)
                self.perform_insert(entry, text + old_text, pos + 2)
                return

        if text == "." and pos == 1:
            if "." not in old_text and old_text[0] == "-":
                text = "0."
                # print(text + old_text)
                pre_text = old_text[:pos]
                post_text = old_text[pos:]
                # print(pre_text, post_text)
                new_text = pre_text + text + post_text
                new_pos = pos + len(text)
                self.perform_insert(entry, new_text, new_pos)
                return

        if text == "." and "." not in old_text:
            pre_text = old_text[:pos]
            post_text = old_text[pos:]
            # print(pre_text, post_text)
            new_text = pre_text + text + post_text
            new_pos = pos + len(text)
            self.perform_insert(entry, new_text, new_pos)
            return

        # All "." scenario have been processed. Reject any more.
        # E.g. Old text already has a decimal point.
        if text == ".":
            # Do nothing.
            self.perform_insert(entry, old_text, pos)
            return

    def perform_insert(self, entry, new_text, new_pos):
        """Perform the text insertion via GObject.idle_add()"""
        entry.handler_block_by_func(self.cb_f1_entry_1_insert_float)
        entry.set_text(new_text)
        entry.handler_unblock_by_func(self.cb_f1_entry_1_insert_float)

        GObject.idle_add(entry.set_position, new_pos)

        entry.stop_emission("insert_text")
        return

    def cb_f1_entry_1_changed(self, entry_widget):
        """Entry filter to ensure entry charcters are integer or float."""
        print("Got here changed")
        # Not implemented.

    def cb_f1_entry_1_activate(self, entry_widget):
        """Entry Widget. Got here upon typing the enter key"""
        # print("Got here activate")
        # print(entry_field.get_text())
        radius = float(entry_widget.get_text())
        print(radius)


if __name__ == "__main__":
    print("Gtk Program started")

    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
    sys.exit("Gtk Program finished")


'''
Links:

https://stackoverflow.com/questions/40074977/how-to-format-the-entries-in-gtk-entry/40163816

https://python-gtk-3-tutorial.readthedocs.io/en/latest/

https://bugzilla.gnome.org/show_bug.cgi?id=644927
'''

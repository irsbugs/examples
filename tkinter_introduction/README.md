# Tkinter - Python Interface for the Widget Toolkit library Tk.

## Introduction to using tkinter.

Wikipedia: https://en.wikipedia.org/wiki/Tk_(software)

Initially released in 1991 this widget toolkit provides the elements for building graphical user interface applications. The Tk library and the python module tkinter are normally included with a python installation.
 
The quick check to test if your computer has tkinter is to run python and enter...

```
>>> import tkinter
>>> dir(tkinter)
```

If tkinter is not installed, then, depending on your platform, proceed with installing it. For example on a Debian Linux based system: `$ sudo apt-get install python3-tk`

Typing the following will launch a GUI window...

```
>>> tkinter.Tk()
```


While there are many choices of widget toolkits for [GUI programming in python](https://wiki.python.org/moin/GuiProgramming), as tkinter is traditionally bundled with python, then it is recommended as the toolkit to initially use to familiarise yourself with GUI programming. 
 
For reference material on programming tkinter:

[Graphical User Interfaces with Tk](https://docs.python.org/3/library/tk.html) at  Python.org.

[Tkinter 8.5 reference: a GUI for Python](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html) by John W. Shipman - New Mexico Tech. 


The following are programs designed to help with understanding and being able to write your first GUI programs in python/tkinter.

* 01_tkinter_a.py through _h.py

    These 9 programs are to demonstrate creating a Tk window. These programs should be run by python from a console window, and also by double-clicking the file name to auto-launch the program so any differences in behaviour may be observed. The programs demonstrate using delay mechanisms to keep displaying the window and introduce the mainloop() function. They also demonstrate adding a title, changing the background colour, changing the geometry, etc.  

* 02_tkinter_no_class_a.py 

    This program does not use the class construct to display a window. As the label and buttons are not instantiated they can not be accessed globally. It is therefore necessary to loop through the widgets in the mainframe until a name match locates the label and its text can then be changed.

* 02_tkinter_no_class_b.py

    This program does not use the class construct to display a window. The Tk toolkits string variable feature is used, which in turn is associated to the textvariable attribute of the label. The buttons may then change the text in the label by setting the contents of the string variable.

* 03_tkinter_class.py

    This program uses a class construct. Within the class are the callback methods for buttons to change the text on the label. The New Zealand secondary school curriculum contains the subject `Digital Technologies.` For NCEA Level 3 this contains unit [91637](www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/2014/as91637.doc) which requires a student to `Develop a complex computer program for a specified task.` A requirement is to use a class construct. This program may be suitable as a template for writing a program that meets this set of NCEA specifications.


Ian Stewart - 2016 July  
<p xmlns:dct="http://purl.org/dc/terms/">
<a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/">
<img src="https://licensebuttons.net/p/zero/1.0/88x31.png"
     style="border-style: none;" alt="Public Domain Mark" />
</a>
</p>

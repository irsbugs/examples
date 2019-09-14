# Launching Python on Windows
Links: [Github](https://github.com/irsbugs/examples/blob/master/windows_extensions/README.md) or [Website](https://irsbugs.github.io/examples/windows_extensions/) 
## The .py and .pyw extensions

On the Windows platform python scripts may be saved with either `.py` or `.pyw`
extensions. Double-clicking on a python file will load the file and python will
commence executing the script.

If the extension is `.py` a console window is opened and the python script
executes within this window. Once the script completes the console window is
closed. So that any output to the console window may be observed before the
window closes, then a delay needs to be added to the program to prevent its
immediate termination. For example, at the end of the python script add...

```
input("Hit Return key to exit program")
```

If the python script produces a GUI window (e.g. uses tkinter), then save the
script with a `.pyw` extension. When this launches no console window will be
opened. Only the GUI window will be displayed. This window will remain open
until terminated with a mouse click to close the window.

While developing a GUI script, it may be helpful to have debugging information
sent to a console window. If the GUI program under development is given a `.py`
extension, then a console window is also provided when the program is launched
and the GUI window is displayed. This console window will display output from a
`print()` function.

The following programs are included to highlight these features when
double-clicking to launch the programs on a Windows platform.

* 01_fibonacci.py

  Launches console window, executes and closes window. This happens too quickly
  to be able to view the fibonacci series of numbers that are generated.

* 02_fibonacci_pause.py

  Launches console window, executes and then pauses, waiting for Return key to
  be hit before it closes.

* 03_fibonacci_tkinter.pyw
 
  Launches a tkinter GUI window. Clicking on a button generates and displays
  the fibonacci series in a label.

* 04_fibonacci_tkinter.py

  Launches the tkinter GUI window and a console terminal window. Clicking on a
  button displays the fibonacci series in a label, plus the `print()` function
  issues debugging information which is sent to the console terminal window.

The launchers are located in C:\Windows\ as the applications `py.exe` and
`pyw.exe`. For more information on Python Launcher for Windows, see [PEP 397](https://www.python.org/dev/peps/pep-0397/).


* Author: Ian Stewart.
* Date: 2016 July
* Scripts are licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/


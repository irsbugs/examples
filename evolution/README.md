# Evolution of a Python Program

## Presentation Slide show

* `evolution_of_a_python_program.opd`

A LibreOffice Impress presentation slide show. The objective of this presentation is to help with educating those who are new to writing python programs. It demonstrates how a python program evolves to have a structure that provides ease of comprehension of the code, built in documentation and testing, and meets PEP8 standards, etc. The presentation contains an appendix to provide an explanation of the some of the code that is added as the program evolves. The presentation contains snippets of the code from the files listed below.

## Files
* `circle_01.py` through to `circle_10.py`. These programs all calculate the area of a circle. `circle_01.py` is the simplist python code. Each program then adds enhancements to the previous program.

* `main_prog_04.py` and `main_prog_05.py` are programs that demonstrate the ability to import as modules `circle_04.py` and `circle_05.py`. 

* `main_prog_05_test.py` imports `circle_05_test.py`. These programs demonstrate that `circle_05_test.py` will normally be a module for `main_prog_05_test.py`. However `circle_05_test.py` has the ability to use *doctest* in its *docstring* to test its function is calculating correctly. Appendix 5 of the presentation describes the use of *doctest*.

* `sys_argv_example.py` is a program designed to demonstrate how the sys module has the ability to provide a list of the arguments from the command line.

* `float_input.py`. In the main slide show presentation there wasn't the space on the slides to show a good method of capturing either an integer or floating point value from a user. This snippet of code provides a more reliable way to capture this user input.


First presented at Hamilton Python User Group meeting by  
Ian Stewart - 12 September 2016

<p xmlns:dct="http://purl.org/dc/terms/">
<a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/">
<img src="https://licensebuttons.net/p/zero/1.0/88x31.png"
     style="border-style: none;" alt="Public Domain Mark" />
</a>








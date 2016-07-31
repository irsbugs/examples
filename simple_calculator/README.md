# Simple Calculator

## Introduction

This python3 program, using the tkinter GUI, provides a four function calculator. 

The approach taken is to have the entry of the numeric keypad data stored as a string. The module [decimal](https://docs.python.org/3/library/decimal.html) is then employed to convert the string data to decimal floating point when performing a calculation. 

With pythons builtin binary floating point, numbers like 1.1 and 2.2 do not have exact representations. The result of adding 1.1 and 2.2 is as follows  

```
    >>> a = 1.1 + 2.2
    >>> type(a)
    <class 'float'>
    >>> print(a)
    3.3000000000000003
```

Using the Decimal module the addition is as follows

```
    >>> from decimal import *
    >>> b = Decimal("1.1") + Decimal("2.2")
    >>> type(b)
    <class 'decimal.Decimal'>
    >>> print(b)
    3.3
```

The calculator contains a two line display. The top line is the equation the bottom line, once the equals key is clicked, is the result. The menu bar has `File --> Output Calculations.` This will output a calculation to the console window.

With division, if the divisor is zero, execution is blocked to prevent attempting a division by zero. In clicking on the equals key the calculation is not attempted and an error message is sent to the console terminal. If the next key clicked on after a division by zero attempt is numeric the calculator responds as if a `clear` had been pressed and it is a new equation being entered.

## Files
* simple_calculator.py

## New Zealand - NCEA.
The New Zealand secondary school curriculum includes the subject Digital Technologies. This program may serve as an introductory guide for writing a program to meet the specifications of the NCEA Level3 Digital Technologies Unit 91637 titled "Develop a complex computer program for a specified task".


Ian Stewart - 2016 April  

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


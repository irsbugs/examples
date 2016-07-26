#!/usr/bin/env python3
#!
print("Fibonacci series...")
fibonacci_list = [0,1]
for i in range(1,15):
    fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i])
print(fibonacci_list)
input("Hit Return key to exit")
                          
"""
Fibonacci series with .py extension - Uses console window, but pauses so the
console window may be read and close once Return key is hit.

When the file is double-clicked to launch it will open a console window,
display the fibonacci series, and then display the message "Hit Return key to
exit". This provides time to view the fibonacci numbers which are the output
of the program.

Author: Ian Stewart.
Date: 2016 July
This script is licensed CC0 https://creativecommons.org/publicdomain/zero/1.0/
         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
"""

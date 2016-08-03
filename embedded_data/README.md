# Embedded Data in a Python Program

## A Python Program that creates a Python Program which includes Embedded Data

A python3 program that is used to read string data from a file where the data is newline delimited. E.g. The word list from a dictionary file, which on many linux systems is `/usr/share/dict/british-english` or `/usr/share/dict/american-english`

The list of words is converted to bytes, compressed and converted to a string of hex characters. The length of the hex string is approximately half the size of the original word list.

A new python3 program is created with this hex data embedded in the program.

On launching the new program it will access its embedded hex data and present this data as a list. The intension is that the new program is edited and you create your own application which utilizes the list extracted from the embedded data.

## Files
* embedded_data.py
  


MIT Licence  
Ian Stewart - 2016 August



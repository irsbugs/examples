#!/usr/bin/env python3
#
# Program: embedded_data.py
#
# Create a template python program that includes compressed data as a hex 
# string. Later the program will recover the data as a list.
#
# The following code will read from a selected file that contains a list of
# words delimited with the newline character. e.g. A dictionary word list file.
#
# The data is read into a list and then converted into comma separated string. 
# The string is converted to bytes, then compressed, then each byte is 
# extracted as a pair of hex nibbles. The hex nibbles are concatinated to 
# build a single string of hex.
# 
# A new python program is created which, when launched, will return the the
# embedded data as a list suitable for use in an application you write in this
# new program. 
#
# The MIT License (MIT)
# Copyright (c) 2016 Ian Stewart
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
# sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.

# import modules
import zlib
import sys
import time

# Constants.
PROMPT_FILE = "/usr/share/dict/british-english"
PROGRAM_NAME_PROMPT = "program_embedded_data.py"
DEBUG = True

# Check python3
if int(sys.version[0]) < 3:
    sys.exit("Python version not supported. Please use python3")

# Prompt for input data file and test that it exists
def get_input_file():
    """Get input data. Newline delimited data."""
    while True:
        file_name = input("Enter data file that uses newline delimter [{}]"
                          .format(PROMPT_FILE))
        if file_name == "":
            file_name = PROMPT_FILE
        try:
            f = open(file_name, "r")
            #print("Opened {} file ok".format(file_name))
            f.close()
            break
        except:
            print("File not found. Please re-enter.")
            continue
    return file_name

def get_program_name():
    """Name for the new program that is created."""
    while True:
        program_name = input("Enter the name for the program [{}] "
                          .format(PROGRAM_NAME_PROMPT))
        if program_name == "":
            program_name = PROGRAM_NAME_PROMPT
        try:
            # Create an empty file. Overwrite any existing file with same name
            f = open(program_name, "w")
            f.close()
            break
        except:
            print("Unable to create {}. Exiting...".format(program_name))
            sys.exit()
    return program_name

def create_hex(file_name):
    """
    Read data file to list. Convert list to string. Encode to bytes.
    Compress bytes. Create hex string of the compressed data.
    """
    f = open(file_name, "r")
    if DEBUG: print("Getting file data as a list with newlines stripped...")
    data_list = f.read().splitlines()
    if DEBUG:print("Total words in list:", len(data_list))
    #print(data_list)

    if DEBUG: print("\nConvert list to a comma separated string...")
    data_string = ""
    start_time = time.time()
    data_string = ",".join(data_list)
    #print(data_string)
    if DEBUG: print("Duration:{:.3f}".format(time.time() - start_time))
    if DEBUG: print("Dictionary string length:", len(data_string))

    if DEBUG: print("\nEncoding string to bytes...")
    start_time = time.time()
    data_string_bytes = str.encode(data_string)
    if DEBUG: print("Duration:{:.3f}".format(time.time() - start_time))
    if DEBUG: print("Dictionary_byte string_length:", len(data_string_bytes))

    if DEBUG: print("\nCompressing bytes string...")
    start_time = time.time()
    data_compressed = zlib.compress(data_string_bytes)
    if DEBUG: print("Duration:{:.3f}".format(time.time() - start_time))
    if DEBUG: print('Compressed binary string length:', len(data_compressed))

    if DEBUG: print("\nCreate a string of 32 hex nibble pairs per line...")
    start_time = time.time()
    count = 0
    line_string = ""
    total_string = ""
    for i in range(len(data_compressed)):
        hex_string = "{:02x}".format(data_compressed[i])    
        line_string = line_string + hex_string
        count += 1
        if count == 32:
            total_string = ("{}    '{}'\\\n".format(total_string, line_string))       
            line_string = ""        
            count = 0
    total_string = ("{}    '{}'\n".format(total_string, line_string))

    #if DEBUG: print(total_string)
    if DEBUG: print("Duration:{:.3f}".format(time.time() - start_time))
    if DEBUG: print("Total hex string length:",len(total_string))

    return total_string
    

def create_program(total_data, program_name):
    """Output the code and data to make a new program"""
    if DEBUG: print("\nWriting program: {}".format(program_name))
    start_time = time.time()
    f = open(program_name, "a")
    f.write(SHEBANG)
    f.write("# Program: {}\n".format(program_name))
    f.write(INTRO)
    f.write(IMPORTS)
    f.write(APPLICATION)
    f.write(MAIN)
    f.write(DATA_PREFIX)
    f.write(total_data)
    f.write(DATA_SUFFIX)
    f.write(LAUNCHER)
    f.close()
    if DEBUG: print("Duration:{:.3f}".format(time.time() - start_time))
    print("Completed generating python program with embedded data: {}"
          .format(program_name))

def main():
    """
    Get the data file and a new program name.
    Compress data and convert to hex string.
    Create a new program with the embedded hex data.
    The new program will extract the data to a list.
    Demo code in the new program performs some basic checks of the data.
    Develop your application that uses the data in the newly created program. 
    """
    file_name = get_input_file()
    program_name = get_program_name()
    total_string = create_hex(file_name)
    create_program(total_string, program_name)

# Constants used to create sections of the new program...
SHEBANG = """#!/usr/bin/env python3
#
"""

INTRO = """#
# A program that contains a list embedded as hex bytes.
# A demonstration application tests the list of data was recovered OK.
#
# Auto-generated data-embedding code subject to The MIT License (MIT)
# Copyright (c) 2016 Ian Stewart
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to 
# deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
# sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.
#
"""

IMPORTS = """
# Import Modules
import zlib
import sys

# Constants
DEBUG = False
"""

APPLICATION = """
def application(data_list):
    '''Write your application program here...'''
    print()
    print("Running dummy application...")
    print("The data list contains {} items.".format(len(data_list)))
    print("The data list first item is {}.".format(data_list[0]))
    print("The data list last item is {}.".format(data_list[-1]))
    '''Write your application program here.'''
"""

MAIN = """
def main():
    '''Launch program.'''
    data_list = get_hex_data()
    application(data_list)

"""

DATA_PREFIX = """
# Auto-generated code. Do not edit program code below this point...
def get_hex_data():
    # Get the hex data and convert to a list
    hex_data = ''\\\n"""

DATA_SUFFIX = """
    if DEBUG: print("Converting hex string to compressed binary...")
    compressed_binary = bytearray()
    count = 0
    hex_nibbles = ""
    for i in hex_data:
        hex_nibbles = hex_nibbles + (str(i))
        count += 1
        if count == 2:
            #print(hex_nibbles)  
            compressed_binary.append(int(hex_nibbles, 16))   
            count = 0
            hex_nibbles = ""
    #print(compressed_binary)
    if DEBUG: print("Compressed binary -bytes:", len(compressed_binary))    

    if DEBUG: print("Uncompressing bytes string...")
    uncompressed_binary = zlib.decompress(compressed_binary)
    if DEBUG: print('Uncompressed Binary -bytes:', len(uncompressed_binary))

    if DEBUG: print("Decoding from bytes and recover as a string...")
    dict_string_recovered = bytes.decode(uncompressed_binary)
    if DEBUG: print("Dict String recovered -bytes:", len(dict_string_recovered))

    if DEBUG: print("Convert string to list")
    dict_list = dict_string_recovered.split(",")
    if DEBUG: print("Dictionary_list -words:", len(dict_list))
    #print(dict_list)
    return dict_list
"""

LAUNCHER = """
if __name__ == "__main__":
    '''Call main routine to launch program.'''
    main()
"""

HELP_INFO = """
embedded_data.py is a python3 program that is used to read string data from a 
file where the data is newline delimited. E.g. The word list from a dictionary 
file. 

The list of words are compressed and converted to a string of hex characters.

A new program is created with this hex data embedded in the program.

Launching the new python3 program will extract the data and present it as a 
list. The new program is designed to be edited and you create your own 
application which utilizes the list extracted from the embedded data.

"""
if __name__ == "__main__":
    """Launch main program or display help"""
    if len(sys.argv) == 2:
        if "-h" in sys.argv[1]:
            print(HELP_INFO)
            sys.exit()
    print("Launching program. For information restart with --help option")
    # Call main program execution
    main()


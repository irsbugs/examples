#!/usr/bin/python3
# -*- coding: utf-8 -*-
# crossword_cracker.py
#
# Objective:
# To demonstrate the use of radiobuttons using tkinter
# The radio buttons are placed into two lists. The index of the list is used
# to point to specific buttons. The Selection from one group of radio buttons
# is passed to the selected button in the other group. 
#
# The linux English dictionary is used and based on a given word length and 
# using the main buttons with characters inserted as filters, all words that
# match are displayed. This may be a handy tool to use when doing the Code
# Cracker puzzle or in solving a Crossword.
#
# Tkinter provides variable (which is global) to be assigned to each widget.
# If this is an IntVar for a group of buttons, then using a .get() will
# supply an integer that may be used as the pointer in the list. E.g.
# self.main_button_list[main_button_group.get()].deselect() would deselect
# the currently selected button.
#
# 2014 November
# Ian Stewart.
# License CC BY-SA http://creativecommons.org/licenses/by-sa/4.0/
#
# Reference material:
# http://effbot.org/tkinterbook/radiobutton.htm
# http://www.python-course.eu/tkinter_radiobuttons.php
# http://www.asciitable.com/index/asciifull.gif
# http://www.tcl.tk/man/tcl8.5/TkCmd/contents.htm
# http://www.tcl.tk/man/tcl8.5/TkCmd/font.htm#M32
# http://www.tutorialspoint.com/python/tk_scrollbar.htm
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/grid-config.html
# http://www.tkdocs.com/tutorial/grid.html
#
__program__ = 'crossword_cracker.py'
__version__ = "1.0"
__date__ = "2014-11-19"
import sys
import time
#print (sys.stdout.encoding)
# Need # -*- coding: utf-8 -*- in line 2 for python2 in case there are some 
# French words with é in the dictionary, (e.g. éclair, éclairs, éclat, élan,...)
#
# Load tkinter depending on V2 or V3 of python. print(sys.version[0])
# Only tkinter is used. Not using the themed tkinter (ttk).

# Exit if python less than version 2.7.0. Use older % instead of .format
if sys.hexversion < 0x02070000:  #Python 2.7.0
    print ('Upgrade: Version %s of python not supported. Exiting...' %
        sys.version[0:sys.version.find(" ")])
    #print('Version {0} of python not supported. Exiting...'.format(
    #    sys.version[0:sys.version.find(" ")]))
    sys.exit()

# Select the correct tkinter.
if sys.hexversion < 0x03000000:  #Python 3.0.0 = 0x03 00 00 00
#if sys.version[0] == '2':
    try:
        from Tkinter import *
    except ImportError as error:
        print('Python2 Tkinter.\n', error)
        sys.exit()
else:
    try:
        from tkinter import *
    except (ImportError) as error:
        print('Python3 tkinter.\nImport Error:', error)
        sys.exit()

#===== Define variables =====
# Note: IntVar() and StringVar() become global variables of tkinter once a
# Tk() window has been initated. Upon selecting the button group variable 
# a .get() will retrieve the selected buttons 'value' option.
global word_list
word_list = []
dictionary_list = []
#word_length_list = []
valid_character = [] #[0,'w'],[5,'a']] is [main word position, character]

# The follow are globally defined at creation of their associated widgets
#global main_button_group
#global spin_value_var
#global alphabet_var

#===== Constants =====
WINDOW_TITLE = ('Crossword Puzzle and Code Cracker tool')

MAIN_BUTTON_COUNT_MAX = 21
MAIN_BUTTON_COUNT_DEFAULT = 10
# For the linux platform the built in Dictionary may be used
#DICTIONARY_FILE = '/usr/share/dict/british-english'
# Alternatively use a seperate dictionary file in the working directory.
DICTIONARY_FILE = 'dictionary-british-english'
# Establish the colour scheme. Using TK and not ttk, so no theme/style.
WINDOW_BACKGROUND = 'blue'

# Main word unselected buttons colour scheme
NUM_BG_COLOUR = 'red'
NUM_BG_A_COLOUR = 'yellow'
NUM_FG_COLOUR = 'blue'
NUM_FG__A_COLOUR = 'red'
#background = NUM_BG_COLOUR, activebackground = NUM_BG_A_COLOUR,
#foreground = NUM_FG_COLOUR, activeforeground = NUM_FG__A_COLOUR

# Main word selected buttons colour scheme
ALPHA_BG_COLOUR = 'green'
ALPHA_BG_A_COLOUR = 'yellow'
ALPHA_FG_COLOUR = 'orange'
ALPHA_FG__A_COLOUR = 'red'
#background = ALPHA_BG_COLOUR, activebackground = ALPHA_BG_A_COLOUR,
#foreground = ALPHA_FG_COLOUR, activeforeground = ALPHA_FG__A_COLOUR

#==== End of defining variables =====

class MainGUI(Frame):
    '''
    Launch the main GUI window and create the widgets.
    '''
    def __init__(self, parent):
        Frame.__init__(self, parent, background=WINDOW_BACKGROUND)
        self.parent = parent
        self.initUI()
     
    def initUI(self):
        self.parent.title(WINDOW_TITLE)
        
        #===== Grid Padding =====
        # The grid is 5 x rows x 30 columns.  
        self.columnconfigure(0, pad=10, minsize=10) # blank padding column
        # Column 1 for Labels, Reset button, and Text
        
        # Column 2 to 29 for alphabet plus blank, and text 
        for i in range(27):
            self.columnconfigure(i + 2, pad=3)
        
        # Column 30 for scrollbar    
        self.columnconfigure(30, pad=10)
        
        for i in range(4):
            self.rowconfigure(i, pad=20)

        #===== Create Label1 for selecting Buttons count =====
        label1 = Label(self,
            text="Length of Word:",
            font='arial 12 normal',
            background='blue',
            foreground='white'
            )

        label1.grid(row=0, column=1, columnspan=1, padx=0, sticky=W)

        #===== Create Label2 for Main Buttons selected =====
        label2 = Label(self,
            text="Select character:",
            font='arial 12 normal',
            background='blue',
            foreground='white'
            )

        label2.grid(row=2, column=1, columnspan=1, padx=0, sticky=W)

        #===== Create Label3 for count of words matched =====
        
        # Needs self prefix as it will be called in a function
        self.label3 = Label(self,
            text="",
            font='arial 12 normal',
            background='blue',
            foreground='white'
            )

        self.label3.grid(row=3, column=1, columnspan=10, padx=0, sticky=W)
        #self.label3.configure(text="")
        
        #===== Create Text box ======
        self.text1 = Text(self,
            font='arial 12 normal',
            wrap='word',
            height=15,
            padx=10,
            relief='sunken',
            borderwidth=2
            )
            #width=50, <_- not necessary as sticky is W+E+S
            
        self.text1.grid(row=4, column=1, columnspan=29, padx=0, pady=10,
        sticky='nswe')
        #self.text1.grid(row=4, column=0, columnspan=27, sticky=W)

        # Call routine to display intro text
        #self.add_text() - Done later
        #===== Create Scrollbar for Text1 ======
            # create a Scrollbar and associate it with txt
        scrollbar1 = Scrollbar(self, command=self.text1.yview)
        scrollbar1.grid(row=4, column=30, pady=10, padx=0, sticky='nsw')
        self.text1['yscrollcommand'] = scrollbar1.set
        
        
        #===== Create Button to Reset the Main buttons =====
        self.button1 = Button(self,
            text="Reset",
            command=self.clear_button
            )

        self.button1.grid(row=1, column=1, padx=10)
        # Trick: Insert a typo to get all the options displayed. E.g...
        #bad option "-aticky": must be
        # -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row,
        # -rowspan, or -sticky

        #====== Create Spinbox =====
        global spin_value_var
        spin_value_var = IntVar()
        spin_value_var.set(MAIN_BUTTON_COUNT_DEFAULT)  # set initial value
        # Note that "from" is a reserved Python keyword.
        # To use this as a keyword argument, add an underscore "from_"
        spinButton = Spinbox(self,
            from_=1,
            to=MAIN_BUTTON_COUNT_MAX,
            increment=1,
            width=2,
            font='arial 12 normal',
            textvariable=spin_value_var,
            command=self.spinbox_change
            )

        spinButton.grid(row=0, column=2, columnspan=2, sticky=W)

        #===== Create all the main Buttons =====
        global main_button_group
        main_button_group = IntVar()

        # Use a button list (i.e. array) instead of individual button names.
        self.main_button_list = []

        for i in range(MAIN_BUTTON_COUNT_MAX):
            main_button = Radiobutton(self,
                text=str(i + 1),
                indicatoron=0,
                width=2,
                padx=1,
                pady=1,
                font='arial 14 italic',
                relief='ridge',
                state='normal',
                background=NUM_BG_COLOUR,
                activebackground=NUM_BG_A_COLOUR,
                foreground=NUM_FG_COLOUR,
                activeforeground=NUM_FG__A_COLOUR,
                variable=main_button_group,
                command=self.main_button_selected,
                value=i
                )

            # Append button to the list so it is addressable by index of list
            self.main_button_list.append(main_button)

            # Postion the button in the grid. Could use...
            # main_button.grid(row = 1, column = 2 + i, sticky=W)
            # ...but now able to make use of the list...
            self.main_button_list[i].grid(row=1, column=2 + i, sticky=W)

        # Button 0 has been set by default initialization action which is
        # equivalent to: main_button_group.set(0). De-select button 0.
        #print(main_button_group.get()) # Returns 0.
        self.main_button_list[0].deselect()

        # All buttons are now displayed.
        # Call the routine to set the displayed buttons to spinbox value.
        self.spinbox_change()

        #===== Create all the Alphabet buttons =====
        global alphabet_var
        alphabet_var = IntVar()
        # default is to initializing 0. i.e. var.set(0), if unspecified
        #var.set(2)  # initializing the choice.

        # Build the list for supplying the alphabet buttons.
        # [('a', 0), ('b', 1), ('c', 2), ... ('y', 24), ('z', 25), ('{', 26)]
        alphabet = []
        for x in range(27):  # alphabet + "blank"
            alphabet.append((chr(97 + x), x))

        #print(alphabet)
        self.alphabet_list = []

        for txt, val in alphabet:
            #print(val)
            alphabet_button = Radiobutton(self,
                text=txt,
                font='arial 14 normal',
                indicatoron=0,
                width=2,
                padx=1,
                pady=1,
                state='disabled',
                relief='ridge',
                underline=-1,
                variable=alphabet_var,
                command=self.character_selected,
                value=val
                )

            alphabet_button.grid(row=2, column=2 + val, sticky=W)

            self.alphabet_list.append(alphabet_button)

        #print(self.alphabet_list.count)
        # Make the last alphabet button a blank (i.e. a space character)
        self.alphabet_list[26].configure(text=' ')
        # First button defaults to being selected. De-select it.
        self.alphabet_list[0].deselect()

        # Call the introduction text
        self.add_text()
        
        # Required at the end of using .grid
        self.pack()
                
        #===== End of initUI(self): setting up window====

    def spinbox_change(self):
        '''
        Change the number of main buttons that are displayed.
        Use .grid_remove() to allow restoring with .grid().
        Do not use .grid_forget() or restore has lost grid position.
        Call function that uses global variable spin_value_var.get() to get
        new list of words of desired length.
        Copy list or words to text box and provide word count in label.
        '''
        # Insert a waiting cursor. Implementation requires Self.update()
        self.config(cursor='watch')
        self.update()
        
        #print(spin_value_var.get())

        # Display .grid(). Main buttons to be displayed 
        for i in range(0, spin_value_var.get()):
            self.main_button_list[i].grid()

        # Hide .grid_remove(). Main buttons to be hidden
        for i in range(spin_value_var.get(), MAIN_BUTTON_COUNT_MAX):
            self.main_button_list[i].grid_remove()

        # Adjust the word list based on spinbutton
        #global word_list  # Todo: no need to be global. Right???
        
        # Call
        update_matched_word_full(self)
        
        # Restore to normal arrow cursor
        self.config(cursor='')
        self.update()
        
    def main_button_selected(self):
        '''
        A button in the main button set has been clicked on.
        Enable the alphabet row of buttons.
        '''
        for i in range(0, len(self.alphabet_list)):
            self.alphabet_list[i].configure(state='normal')

        #print(word_list)
        
    def character_selected(self):
        '''
        A character from a to z has been selected to fill a selected
        position in the main buttons. Or the "blank" has been selected to
        deselect this postion in the main buttons from having any alphabetic
        character displayed.
        '''
        # Insert a waiting cursor. Self.update() is required to implement
        self.config(cursor='watch')
        self.update()
                
        # Get the text from the alphabet button selected and copy it to the
        # selected main button.
        # However, if the "blank" alphabetic button is clicked, insert
        # numeric position in the main button.

        if alphabet_var.get() == len(self.alphabet_list)-1:
            # "blank" selected. Display main word button with numeric position
            self.main_button_list[main_button_group.get()].configure(
                text=str(main_button_group.get() + 1))
            # Set the numbers colour scheme
            self.main_button_list[main_button_group.get()].configure(
                font='arial 14 italic',
                background=NUM_BG_COLOUR,
                activebackground=NUM_BG_A_COLOUR,
                foreground=NUM_FG_COLOUR,
                activeforeground=NUM_FG__A_COLOUR)
                
            # Call full update. 
            update_matched_word_full(self)

        else:
            # Display main button with the alphabetic text
            ''' Todo: Fix bug with switching preselected main button
                need to do full search. Use background colour as test?
            '''
            self.main_button_list[main_button_group.get()].configure(
                text=self.alphabet_list[alphabet_var.get()].cget('text'))
            # Set the alphabet colour scheme
            self.main_button_list[main_button_group.get()].configure(
                font='arial 14 bold',
                background=ALPHA_BG_COLOUR,
                activebackground=ALPHA_BG_A_COLOUR,
                foreground=ALPHA_FG_COLOUR,
                activeforeground=ALPHA_FG__A_COLOUR)
                
            # Partial word matching routine. 
            # Improves performance as exiting (filtered) word_list is used   
            #update_matched_word_partial(self)    #< change to _full workaround
            update_matched_word_full(self)    #< change to _full workaround


        # De-select the main button
        self.main_button_list[main_button_group.get()].deselect()

        # Disable the alphabet list after adding a character to the main word
        for i in range(0, len(self.alphabet_list)):
            self.alphabet_list[i].configure(state='disabled')
            self.alphabet_list[i].deselect()

        # Restore to normal arrow cursor
        self.config(cursor='')
        self.update()
        
    def clear_button(self):
        '''
        Set all the main buttons back to their original colours
        # Could use: range(0,MAIN_BUTTON_COUNT_MAX -1), better to use the list.
        '''
        for i in range(len(self.main_button_list)):
        #for i, j in enumerate(self.main_button_list):
            # reset the colour scheme
    
            self.main_button_list[i].configure(
                text=str(i + 1),
                font='arial 14 italic',
                background=NUM_BG_COLOUR,
                activebackground=NUM_BG_A_COLOUR,
                foreground=NUM_FG_COLOUR,
                activeforeground=NUM_FG__A_COLOUR
                )
            # Ensure all main buttons are deselected.
            self.main_button_list[i].deselect()

        # Ensure the alphabet buttons are disabled
        for i in range(0, len(self.alphabet_list)):
            self.alphabet_list[i].configure(state='disabled')
            self.alphabet_list[i].deselect()

        # Call full update
        update_matched_word_full(self)
        
    def add_text(self):
     
        self.text1.insert('1.0', '''Buttons in a List #3 - Python notes:

        Click on the Reset button to clear this text and commence.
         
        The Linux British English dictionary should be located in: 
        /usr/share/dict/british-english. Alternatively use a dictionary
        file that is placed in the same directory as this program.
        
        Based on a given word length and using the main buttons with 
        characters inserted as filters, all words from the dictionary that
        match are displayed. 
        
        This may be a handy tool to use when doing Code Cracker or 
        Crossword puzzles.

        This program was developed for use on a Linux platform. 
        It was tested with both python2.7 and python3.4 and requires the
        tkinter toolkit.

        Example by Ian Stewart for Hamilton Python Users Group.
        November 2014
        
        ''')
        
        #self.text1.clear()
        
    #===== End of class MainGUI(Frame) =====        
        
# Functions to create filtered dictionary

def update_matched_word_partial(self):
    # Adjust the word list based on spinbutton
    #global word_list  # Todo: no need to be global. Right??? Wrong?

    if sys.hexversion < 0x03030000:  # python 3.3.0
        start_time = time.clock()
    else:
        start_time = time.process_time() 
    
    # Determine which main buttons have filter characters
    del valid_character[:] #.clear()
    
    for i in range(0, spin_value_var.get()):
        # Check if the first character in the button text is alphabetic 
        if ord(self.main_button_list[i].cget('text')[0]) >= 97:
            #print(i, self.main_button_list[i].cget('text'))
            # Build a valid character list. [[0, 'a'], [8, 'a'], [9, 'b']]
            valid_character.append(
                [i, self.main_button_list[i].cget('text')])
            
    #print(valid_character)
      
    # The following code takes time to execute. 
    # Particularly with 8 letter words as there are over 10,000.
    # E.g. valid_character = [[0,'w'],[5,'a']]
    for x in valid_character:
        #print(x)
        # Use reverse order so removing items does not corrupt the index 
        for item in reversed(word_list):
            #print(item[x[0]], x[1])
            #if not item[x[0]] == x[1]:
            if item[x[0]] != x[1]:
                word_list.remove(item)

    #print(word_list)
    # Clear the text box and then update with the list of words
    self.text1.delete('1.0','end')
    for item in word_list:
        self.text1.insert('end', item + ', ')

    if sys.hexversion < 0x03030000:
        end_time = time.clock()
    else:
        end_time = time.process_time()    
    elapsed_time = end_time - start_time
    
    # Update label with statistic on words matched.
    self.label3.configure(text="Words Matched: {0} in {1:.3f} seconds".format(
        len(word_list), elapsed_time))    

    #self.label3.configure(text="Words Matched: {}".format(len(word_list)))    


def update_matched_word_full(self):
    '''
    After every reset or change in word length spinbox
    From the dictionary list, create a word list of the selected length
    spin_value_var.get() is a global variable of the desired word length
    '''
    self.config(cursor='watch')
    
    if sys.hexversion < 0x03030000:
        start_time = time.clock()
    else:
        start_time = time.process_time()    
  
    # Adjust the word list based on spinbutton
    #global word_list  # Todo: no need to be global. Right???
    
    # Determine which main buttons have filter characters
    del valid_character[:] #.clear()

    for i in range(0, spin_value_var.get()):
        # Check if the first character in the button text is alphabetic 
        if ord(self.main_button_list[i].cget('text')[0]) >= 97:
            #print(i, self.main_button_list[i].cget('text'))
            # Build a valid character list. [[0, 'a'], [8, 'a'], [9, 'b']]
            valid_character.append(
                [i, self.main_button_list[i].cget('text')])
            
    #print(valid_character)

    del word_list[:]  # del word_list[:] same as V3 wordlist.clear())
    
    # Create list of words of the desired length based
    for item in dictionary_list[spin_value_var.get() - 1]:   
        #for item in dictionary_list[wordlength -1]:
        word_list.append(item)
    
    # The following code takes time to execute. 
    # Particularly with 8 letter words as there are about 10,000.
    # E.g. valid_character = [[0,'w'],[5,'a']]
    for x in valid_character:
        #print(x)
        # Use reverse order so removing items does not corrupt the index 
        for item in reversed(word_list):
            #print(item[x[0]], x[1])
            #if not item[x[0]] == x[1]:
            if item[x[0]] != x[1]:
                word_list.remove(item)

    #print(word_list)
    # Clear the text box and then update with the list of words
    self.text1.delete('1.0','end')
    for item in word_list:
        self.text1.insert('end', item + ', ')

   
    if sys.hexversion < 0x03030000:
        end_time = time.clock()
    else:
        end_time = time.process_time()    
    elapsed_time = end_time - start_time

    # Update label with statistic on words matched.
    self.label3.configure(
        text="Words Matched: {0} in {1:.3f} seconds".format(
        len(word_list), elapsed_time))    
    
    self.config(cursor='')   
    '''
    Since time.clock() is now deprecated in Python 3.3, you have to use 
    time.perf_counter() (system-wide timing) or time.process_time()
    (process-wide timing), just the way you used to use time.clock():
    '''     

def load_stripped_dictionary():    
    '''
    Open dictionary file and filter out invalid words. i.e. Proper Nouns,
    words that contain an apostrophy, and French words.
    Strip off the new line character after each word.
    Based on the length of the word (1 to 20 characters) move it to a
    dictionary list[[0], ..., [19]]. Words with 21 characters or greater are 
    moved to dictionary list[20].
    '''
    # Template for dictionary[] Consists of 21 lists based on length of word.
    dictionary = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 
        [], [], [], [], [], []]
  
    if file_exists(DICTIONARY_FILE) == False:
        print( '\nError: Dictionary file {0} is unavailable. \n'
            'Exiting...'.format(DICTIONARY_FILE))
        sys.exit()
    
    with open(DICTIONARY_FILE, 'r') as f:
        for word in f:
            # Filter out proper nouns, based on first chacacter is upper case.
            #if not word[0].isupper():
            if word[0].islower():

                # Filter out words with apostrophies
                #if not word.find("'") >= 0:
                if word.find("'") == -1:

                    # Filter out French words. Start with é. 
                    # éclair, éclairs, éclat, élan, émigré, 
                    # émigrés, épée, épées, étude, études
                    # Huh? 'creche' is not in the dictionary. Too French?
                    # Python2 requires 2nd line to be # -*- coding: utf-8 -*-
                    # Otherwise SyntaxError: Non-ASCII character '\xc3' 

                    if word.find("é") == -1:

                        # strip off the \n
                        word = word[0:len(word)-1]

                        # Based on the words length copy it into its list.
                        if len(word) >= 21:
                            #Insert 21 characters or more in [20]
                            dictionary[20].append(word)

                        elif len(word) >= 1 and len(word) <= 20:
                            # Insert 1 to 20 character words in [0] to [19]
                            dictionary[len(word)-1].append(word)

                        else:
                            #ignore any blank lines
                            pass

    #print(dictionary)
    #print(len(dictionary))
    return dictionary

def file_exists(filename):
    try:
        with open(filename, 'r') as f:
            return True
    except IOError:
        return False

def main():
    root = Tk()
    # width x height + screen coordinates +x +y
    #root.geometry("900x300+50+50") #<-- Don't set geometry of window
    app = MainGUI(root)    
    root.mainloop()


if __name__ == "__main__":
    import sys
    print('{0} version {1}. Loading GUI and sorting dictionary...' .format(
        __program__, __version__))

    # From the dictionary file create a global dictionary list.
    # Filtered out are words with apostrophies, proper nouns, french words.
    dictionary_list = load_stripped_dictionary()
    main()
    sys.exit()

'''
Notes:

         1         2         3         4         5         6         7        7
1234567890123456789012345678901234567890123456789012345678901234567890123456789
'''

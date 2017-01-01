#!/usr/bin/env python3
import sys
import platform

_description_ = """
    Review the character set to determine if it includes the box drawing
    set of characters.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_24_a.py

START = 0x20
END = 0x10000
# Start from 32 = 0X20 = space
# 160 = 0xa0 = npsb non-break space ?


def main():
    print("Display Unicode Characters")
    get_platform()

    start = get_integer("Provide the start value of the character range", START)
    end = get_integer("Provide the end value of the character range", END)

    character_set(start, end)
    input("Press Enter key to end program")
    sys.exit()


def get_platform():
    print("Program is running on\nSystem: {}, Release: {}, Version: {}.\n"
          .format(platform.system(), platform.release(), platform.version()))

    if platform.system() == "Windows":
        print("Microsoft Code Page: {}".format(sys.stdout.encoding))
        print("To change code page. C:\>CHCP nnn {}\n")


def get_integer(message="Enter an integer", prompt=0):
    """
    Function to return an integer input from the console or the prompted value.
    The input may be a decimal or hex string. Eg. 23 or 0x23
    The function is optionally supplied an Input message and a prompt value.
    The prompt value may be an integer as decimal or hex (E.g. 23 0x23) or as
    a string (E.g. '23' or '0x23')
    An invalid prompt will be converted to 0.
    An invalid entry will force the User to re-enter the input value.
    The int() function with an argument of "0", converts both decimal and hex
    integer = int("23", 0) or integer = int("0x23", 0)
    """
    while True:
        # Check the prompt
        try:
            hex_prompt = hex(prompt)
            # Prompt is decimal integer, add the hex to the prompt string
            string = input("{} [{} {}]:".format(message, prompt, hex_prompt))
        except TypeError:
            try:
                # Prompt maybe integer or hex string. If so convert to integer
                prompt = int(prompt, 0)
            except ValueError:
                # Prompt can not be determined. Set it to decimal integer 0
                print("Prompt of {} is invalid. Setting to 0.".format(prompt))
                prompt = 0
            string = input("{} [{} {}]:".format(message, prompt, hex(prompt)))
        # Check the User input
        if len(string) > 0:
            try:
                # If either integer string or hex string convert to integer
                value = int(string, 0)
                return value
            except ValueError:
                print("Not an integer. Please re-enter")
                continue
        else:
            # Use the prompt, which has been checked that it is an integer.
            return prompt


def character_set(start=0x2500, end=0x257f):
    "Display characters in the range. Include decimal and hex unicode values."
    print("Display characters in the range: {} to {}. Hex: {} to {}.\n"
          .format(start, end, hex(start), hex(end)))
    print("+-- Character found running number.")
    print("|    +-- Unicode decimal value.")
    print("|    |    +-- Unicode Hex value.")
    print("|    |    |      +-- Displayed Character.")
    print("|    |    |      |")
    print("V    V    V      V")

    counter_1 = 0
    counter_2 = 0
    for value in range(start, end + 1):
        try:
            print("{: <5}{: <5}{: <7}{}".format(counter_1 + 1, value,
                  hex(value), chr(value)))
            counter_1 += 1
        except:
            # print("{: <5}{: <5}{: <7}".format(counter_2, value, hex(value)))
            counter_2 += 1
            pass

    print("\nDisplayable characters:{} Undisplayable:{}. Total:{}. \n"
          .format(counter_1, counter_2, counter_1 + counter_2))


if __name__ == "__main__":
    # Program starts here.
    main()
"""
Example: Running this program on Windows 10 CMD.exe window.

Display Unicode Characters
Program is running on
System: Windows, Release: 10, Version: 10.0.14393.

Microsoft Code Page: cp437
To change code page. C:\>CHCP nnn {}

Provide the start value of the character range [32 0x20]:
Provide the end value of the character range [65536 0x10000]:
Display characters in the range: 32 to 65536. Hex: 0x20 to 0x10000.

+-- Character found number.
|    +-- Unicode decimal value.
|    |    +-- Unicode Hex value.
|    |    |      +-- Displayed Character.
|    |    |      |
V    V    V      V
1    32   0x20
2    33   0x21   !
3    34   0x22   "
4    35   0x23   #
5    36   0x24   $
6    37   0x25   %
7    38   0x26   &
8    39   0x27   '
9    40   0x28   (
10   41   0x29   )
11   42   0x2a   *
12   43   0x2b   +
13   44   0x2c   ,
14   45   0x2d   -
15   46   0x2e   .
16   47   0x2f   /
17   48   0x30   0
18   49   0x31   1
19   50   0x32   2
20   51   0x33   3
21   52   0x34   4
22   53   0x35   5
23   54   0x36   6
24   55   0x37   7
25   56   0x38   8
26   57   0x39   9
27   58   0x3a   :
28   59   0x3b   ;
29   60   0x3c   <
30   61   0x3d   =
31   62   0x3e   >
32   63   0x3f   ?
33   64   0x40   @
34   65   0x41   A
35   66   0x42   B
36   67   0x43   C
37   68   0x44   D
38   69   0x45   E
39   70   0x46   F
40   71   0x47   G
41   72   0x48   H
42   73   0x49   I
43   74   0x4a   J
44   75   0x4b   K
45   76   0x4c   L
46   77   0x4d   M
47   78   0x4e   N
48   79   0x4f   O
49   80   0x50   P
50   81   0x51   Q
51   82   0x52   R
52   83   0x53   S
53   84   0x54   T
54   85   0x55   U
55   86   0x56   V
56   87   0x57   W
57   88   0x58   X
58   89   0x59   Y
59   90   0x5a   Z
60   91   0x5b   [
61   92   0x5c   \
62   93   0x5d   ]
63   94   0x5e   ^
64   95   0x5f   _
65   96   0x60   `
66   97   0x61   a
67   98   0x62   b
68   99   0x63   c
69   100  0x64   d
70   101  0x65   e
71   102  0x66   f
72   103  0x67   g
73   104  0x68   h
74   105  0x69   i
75   106  0x6a   j
76   107  0x6b   k
77   108  0x6c   l
78   109  0x6d   m
79   110  0x6e   n
80   111  0x6f   o
81   112  0x70   p
82   113  0x71   q
83   114  0x72   r
84   115  0x73   s
85   116  0x74   t
86   117  0x75   u
87   118  0x76   v
88   119  0x77   w
89   120  0x78   x
90   121  0x79   y
91   122  0x7a   z
92   123  0x7b   {
93   124  0x7c   |
94   125  0x7d   }
95   126  0x7e   ~
96   127  0x7f   
97   160  0xa0    
98   161  0xa1   ¡
99   162  0xa2   ¢
100  163  0xa3   £
101  165  0xa5   ¥
102  170  0xaa   ª
103  171  0xab   «
104  172  0xac   ¬
105  176  0xb0   °
106  177  0xb1   ±
107  178  0xb2   ²
108  181  0xb5   µ
109  183  0xb7   ·
110  186  0xba   º
111  187  0xbb   »
112  188  0xbc   ¼
113  189  0xbd   ½
114  191  0xbf   ¿
115  196  0xc4   Ä
116  197  0xc5   Å
117  198  0xc6   Æ
118  199  0xc7   Ç
119  201  0xc9   É
120  209  0xd1   Ñ
121  214  0xd6   Ö
122  220  0xdc   Ü
123  223  0xdf   ß
124  224  0xe0   à
125  225  0xe1   á
126  226  0xe2   â
127  228  0xe4   ä
128  229  0xe5   å
129  230  0xe6   æ
130  231  0xe7   ç
131  232  0xe8   è
132  233  0xe9   é
133  234  0xea   ê
134  235  0xeb   ë
135  236  0xec   ì
136  237  0xed   í
137  238  0xee   î
138  239  0xef   ï
139  241  0xf1   ñ
140  242  0xf2   ò
141  243  0xf3   ó
142  244  0xf4   ô
143  246  0xf6   ö
144  247  0xf7   ÷
145  249  0xf9   ù
146  250  0xfa   ú
147  251  0xfb   û
148  252  0xfc   ü
149  255  0xff   ÿ
150  402  0x192  ƒ
151  915  0x393  Γ
152  920  0x398  Θ
153  931  0x3a3  Σ
154  934  0x3a6  Φ
155  937  0x3a9  Ω
156  945  0x3b1  α
157  948  0x3b4  δ
158  949  0x3b5  ε
159  960  0x3c0  π
160  963  0x3c3  σ
161  964  0x3c4  τ
162  966  0x3c6  φ
163  8319 0x207f ⁿ
164  8359 0x20a7 ₧
165  8729 0x2219 ∙
166  8730 0x221a √
167  8734 0x221e ∞
168  8745 0x2229 ∩
169  8776 0x2248 ≈
170  8801 0x2261 ≡
171  8804 0x2264 ≤
172  8805 0x2265 ≥
173  8976 0x2310 ⌐
174  8992 0x2320 ⌠
175  8993 0x2321 ⌡
176  9472 0x2500 ─
177  9474 0x2502 │
178  9484 0x250c ┌
179  9488 0x2510 ┐
180  9492 0x2514 └
181  9496 0x2518 ┘
182  9500 0x251c ├
183  9508 0x2524 ┤
184  9516 0x252c ┬
185  9524 0x2534 ┴
186  9532 0x253c ┼
187  9552 0x2550 ═
188  9553 0x2551 ║
189  9554 0x2552 ╒
190  9555 0x2553 ╓
191  9556 0x2554 ╔
192  9557 0x2555 ╕
193  9558 0x2556 ╖
194  9559 0x2557 ╗
195  9560 0x2558 ╘
196  9561 0x2559 ╙
197  9562 0x255a ╚
198  9563 0x255b ╛
199  9564 0x255c ╜
200  9565 0x255d ╝
201  9566 0x255e ╞
202  9567 0x255f ╟
203  9568 0x2560 ╠
204  9569 0x2561 ╡
205  9570 0x2562 ╢
206  9571 0x2563 ╣
207  9572 0x2564 ╤
208  9573 0x2565 ╥
209  9574 0x2566 ╦
210  9575 0x2567 ╧
211  9576 0x2568 ╨
212  9577 0x2569 ╩
213  9578 0x256a ╪
214  9579 0x256b ╫
215  9580 0x256c ╬
216  9600 0x2580 ▀
217  9604 0x2584 ▄
218  9608 0x2588 █
219  9612 0x258c ▌
220  9616 0x2590 ▐
221  9617 0x2591 ░
222  9618 0x2592 ▒
223  9619 0x2593 ▓
224  9632 0x25a0 ■

Displayable characters:224 Undisplayable:65281. Total:65505.

===

Windows10 - Box Drawing Unicode Characters - Grouped:

Singles
─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

Doubles
═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬

Single horizontal, double vertical
─ ║ ╓ ╖ ╙ ╜ ╟ ╢ ╥ ╨ ╫

Double horizontal, single vertical
═ │ ╒ ╕ ╘ ╛ ╞ ╡ ╤ ╧ ╪


Linux desktop Console Terminal applications (E.g. GNOME Terminal) offer a more
extensive range of box drawing unicode characters.


    Box Drawing set that Windows can display with CP437...

    2500 to 250f
    0 1 2 3 4 5 6 7 8 9 a b c d e f
    ─   │                   ┌

    2510 to 251f
    0 1 2 3 4 5 6 7 8 9 a b c d e f
    ┐       └       ┘       ├

    2520 to 252f
    0 1 2 3 4 5 6 7 8 9 a b c d e f
            ┤               ┬

    2530 to 253f
    0 1 2 3 4 5 6 7 8 9 a b c d e f
            ┴               ┼

    2540 to 254f
    0 1 2 3 4 5 6 7 8 9 a b c d e f


    2550 to 255f
    0 1 2 3 4 5 6 7 8 9 a b c d e f
    ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟

    2560 to 256f
    0 1 2 3 4 5 6 7 8 9 a b c d e f
    ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬

    2570 to 257f
    0 1 2 3 4 5 6 7 8 9 a b c d e f


To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_24_a.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_24_a.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

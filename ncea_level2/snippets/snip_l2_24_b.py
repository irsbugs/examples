#!/usr/bin/env python3
import sys
import time
import platform
import ctypes

# import codecs
# sys.setdefaultencoding('utf-8')

_description_ = """
    Draw four styles of boxes from the Unicode Box Drawing set of characters.
    """
_author_ = """Ian Stewart - December 2016
    Hamilton Python User Group - https://hampug.pythonanywhere.com
    CC0 https://creativecommons.org/publicdomain/zero/1.0/ """

# Program: snip_l2_24_b.py

# Initialise constants
ESC = chr(27)  # Escape character
CSI = ESC + "["  # Control Sequence Introducer
BEL = chr(7)

# Set if you want to pause between screens and hit return to continue
pause = True
delay = True
delay_duration = 0.4
debug = True


def main():
    escape_sequence_check()
    get_platform()
    boxes_character_set()
    input("Press Enter key to end program")
    sys.exit()


def get_platform():
    print("Program is running on\nSystem: {}, Release: {}, Version: {}.\n"
          .format(platform.system(), platform.release(), platform.version()))

    if platform.system() == "Windows":
        print("Microsoft Code Page: {}".format(sys.stdout.encoding))
        print("To change code page. C:\>CHCP nnn {}\n")


def boxes_character_set():
    print("Box Drawings using characters from the range 0x2500 to 0x257f\n")

    # Single top and single sides  ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
    print("Single top and single sides: ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼")
    print(" ┌──────────┐")
    print(" │  Single  │")
    print(" │   Line   │")
    print(" │          │")
    print(" │          │")
    print(" └──────────┘")

    print(" ┌─────┬─────┐")
    print(" │  0  │  1  │")
    print(" │     │     │")
    print(" ├─────┼─────┤")
    print(" │  2  │  3  │")
    print(" │     │     │")
    print(" │     │     │")
    print(" └─────┴─────┘")
    print()

    # Double top and sides ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬
    print("Double horizontal vertical: ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬")
    print(" ╔═════╦═════╗")
    print(" ║     ║     ║")
    print(" ║     ║     ║")
    print(" ║     ║     ║")
    print(" ║     ║     ║")
    print(" ╠═════╬═════╣")
    print(" ║     ║     ║")
    print(" ║     ║     ║")
    print(" ║     ║     ║")
    print(" ╚═════╩═════╝")
    print()

    # Double Top single sides ╒ ╕ ╘ ╛ ╞ ╡ ╤ ╧ ╪
    print("Double lines horizontal, single vertical: ═ │ ╒ ╕ ╘ ╛ ╞ ╡ ╤ ╧ ╪")
    print(" ╒═════╤═════╕")
    print(" │     │     │")
    print(" │     │     │")
    print(" │     │     │")
    print(" ╞═════╪═════╡")
    print(" │     │     │")
    print(" │     │     │")
    print(" ╘═════╧═════╛")
    print()

    # Single top double sides
    # ╓ ╖ ╙ ╜ ╟ ╢ ╥ ╨ ╫
    print("Double lines vertical, single horizontal: ─ ║ ╓ ╖ ╙ ╜ ╟ ╢ ╥ ╨ ╫")
    print(" ╓────╥────╖")
    print(" ║    ║    ║")
    print(" ║    ║    ║")
    print(" ╟────╫────╢")
    print(" ║    ║    ║")
    print(" ║    ║    ║")
    print(" ╙────╨────╜")


def escape_sequence_check():
    """
    Check the platform. If windows 10, then enable Terminal Escape sequences.
    Requires: platform and ctypes modules
    Reads: if debug, if delay, and if pause global variables
    """
    if platform.system() == "Windows":
        if debug: print("Microsoft {} Release: {} Version: {}"
                        .format(platform.system(), platform.release(),
                                platform.version()))
        ver_list = platform.version().split(".")
        if int(platform.release()) < 10:
            print("Requires Windows version 10 or higher for ANSI support.")
            print("Exiting...")
            sys.exit()
        if len(ver_list) >= 2:
            if int(ver_list[2]) >= 10586:
                s = "This version of Win10 supports ANSI escape sequences."
                if debug: print(s)
            else:
                s = ("Win10 requires updating to support ANSI escape "
                     "sequences.\nMinimum version: 10.0.10586 'Threshold 2' "
                     "10 May 2016.")
                print(s)
                # 10.0.14393 is "The Anniversary Update". Released 2 Aug 2016.
                print("Exiting...")
                sys.exit()
        if int(platform.release()) >= 10:
            # import ctypes
            kernel32 = ctypes.windll.kernel32
            status = kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            if status == 0:
                print("Error returned attempting to set ANSI escape sequences")
                print("Continuing, but results are not predictable...")
            else:
                s = "Windows has been set to perform ANSI escape sequences.\n"
                if debug: print(s)
                s = ("For more information on Microsoft use of ANSI escape"
                     "codes\nplease visit this web-page...\n"
                     "https://msdn.microsoft.com/en-us/library/mt638032"
                     "(v=vs.85).aspx")
                if debug: print(s)
        if delay: time.sleep(2)
        if pause: input("\nType Return key to continue")
    else:
        # The Linux platform normally has a console terminal that supports ANSI
        # escape sequences.
        pass


if __name__ == "__main__":
    # Program starts here.
    main()

"""
Windows10
Box Drawing set ...

Singles
─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

Doubles
═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬

Single top double sides
─ ║ ╓ ╖ ╙ ╜ ╟ ╢ ╥ ╨ ╫

Double Top single sides
═ │ ╒ ╕ ╘ ╛ ╞ ╡ ╤ ╧ ╪

Windows 10 sub-set of Unicode Box Drawing set of characters...
9472  0x2500 ─
9474  0x2502 │
9484  0x250c ┌
9488  0x2510 ┐
9492  0x2514 └
9496  0x2518 ┘
9500  0x251c ├
9508  0x2524 ┤
9516  0x252c ┬
9524  0x2534 ┴
9532  0x253c ┼
9552  0x2550 ═
9553  0x2551 ║
9554  0x2552 ╒
9555  0x2553 ╓
9556  0x2554 ╔
9557  0x2555 ╕
9558  0x2556 ╖
9559  0x2557 ╗
9560  0x2558 ╘
9561  0x2559 ╙
9562  0x255a ╚
9563  0x255b ╛
9564  0x255c ╜
9565  0x255d ╝
9566  0x255e ╞
9567  0x255f ╟
9568  0x2560 ╠
9569  0x2561 ╡
9570  0x2562 ╢
9571  0x2563 ╣
9572  0x2564 ╤
9573  0x2565 ╥
9574  0x2566 ╦
9575  0x2567 ╧
9576  0x2568 ╨
9577  0x2569 ╩
9578  0x256a ╪
9579  0x256b ╫
9580  0x256c ╬


    Box Drawing set. Sub-set available with Windows 10 Code Page 437...
    Note: Linux terminal's (E.g. GNOME Terminal) provide the complete Unicode
    Box Drawing set of characters.

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

=====

The following is example code of using the ANSI escape sequences to perform
line drawing. This is not recommended on Windows 10 as the "cross-hairs"
character is not currently supported.

    # Apply foreground and background colours
    #print("{}{}m{}{}m"
    #      .format(CSI, "92", CSI, "42"),
    #      end="", flush=True)

    # n produces a square on Windows, should be a cross-hair graphic.
    # Each print function includes a newline character (\n).
    print(ESC + "(0")  # Line Drawing mode
    print(" lqqqwqqqk")
    print(" x A x A x")
    print(" x 0 x 1 x")
    print(" x   x   x")
    print(" tqqqnqqqu")
    print(" x A x A x")
    print(" x 2 x 3 x")
    print(" x   x   x")
    print(" mqqqvqqqj")
    print(ESC + "(B")  # Ascii character mode

    '''
    With Windows10 the ANSI line drawing fails to do the cross-hairs (i.e. "n")
    Below the "n" is replaced with the Boxes Line Drawing character "┼" 0x253c.
    '''
    print("Line Drawing - Substutute crosshairs character\n{}(0".format(ESC))

    print(" lqqqwqqqk")
    print(" x B x B x")
    print(" x 0 x 1 x")
    print(" x   x   x")

    print(" tqqq", end="", flush=True)
    # Turn off line drawing, add the crosshairs, turn on line drawing
    print(ESC + "(B", end="", flush=True)
    print("┼", end="", flush=True)
    print("{}(0".format(ESC,), end="", flush=True)

    print("qqqu")
    print(" x B x B x")
    print(" x 2 x 3 x")
    print(" x   x   x")
    print(" mqqqvqqqj")

    print(ESC + "(B", end="", flush=True)

To check code style:
Linux...
$ python3 -m pep8 --statistic --ignore=E701 snip_l2_24_b.py
Install pep8 on Linux: $ sudo apt-get install python3-pep8
Windows...
> python -m pep8 --statistic --ignore=E701 snip_l2_24_b.py
Install pep8 on Windows: >pip3 install pep8
More information: https://www.python.org/dev/peps/pep-0008/
"""

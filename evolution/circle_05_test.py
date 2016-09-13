



RADIUS = 10
import math



 
 
 
 
 

def calculate_circle_area(radius):
    """
    Supplied with the radius, calculate the area of a circle.

    >>> calculate_circle_area(10)
    314.1592653589793

    """
    area = math.pi * radius ** 2
    return area

if __name__ == "__main__":
    """Launch circle module as a program for testing."""
    import doctest
    doctest.testmod()  
 
"""
See: https://docs.python.org/3/library/doctest.html

When a program is written to be a module, then add doctest for testing the 
module.

Examples of running the module...

$ python3 circle_05_test.py
    <--- If test passes without error nothing returned. Need -v for verbose 
$ python3 circle_05_test.py -v
Trying:
    calculate_circle_area(10)
Expecting:
    314.1592653589793
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.calculate_circle_area
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

===
Change expected, from: 314.1592653589793 to 314.15926535897930000000000
$ python3 circle_05_test.py
**********************************************************************
File "circle_05_test.py", line 20, in __main__.calculate_circle_area
Failed example:
    calculate_circle_area(10)
Expected:
    314.15926535897930000000000
Got:
    314.1592653589793
**********************************************************************
1 items had failures:
   1 of   1 in __main__.calculate_circle_area
***Test Failed*** 1 failures.

"""
 

                                                                          


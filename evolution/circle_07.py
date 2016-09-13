



# RADIUS = 10
import math


def input_radius():
    """Get User input from the console."""
    radius = input("Enter the radius of the circle: ")
 
 
    return float(radius)

def calculate_circle_area(radius):
    """Supplied with the radius, calculate the area of a circle."""
    area = math.pi * radius ** 2
    return area

if __name__ == "__main__":
    """Launch circle program."""
 
 
 
    radius = input_radius()
    circle_area = calculate_circle_area(radius)
    print(circle_area)
                                                                          






# RADIUS = 10
import math



 
 
 
 
 

def calculate_circle_area(radius):
    """Supplied with the radius, calculate the area of a circle."""
    area = math.pi * radius ** 2
    return area

if __name__ == "__main__":
    """Launch circle program."""
  
 
 
    radius = input("Enter the radius of the circle: ") 
    circle_area = calculate_circle_area(float(radius))
    print(circle_area)
                                                                          


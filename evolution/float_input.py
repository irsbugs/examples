# Reject a string that won't convert to a floating point value.  
# If invalid data entry, then ask for the data again.
def input_radius(prompt):
    """Get User input from the console. Must be integer or floating point"""
    while True:
        radius = input("Enter the radius of the circle [{}]: ".format(prompt))
        if radius == "":
            radius = prompt
        try: 
            return float(radius)
        except ValueError as e:
            print("Error: {}".format(e))
            print("Please re-enter the radius. Enter an integer or a float...")
            continue
        
prompt = 10
radius = input_radius(prompt)
print("Value of radius is {}".format(radius))



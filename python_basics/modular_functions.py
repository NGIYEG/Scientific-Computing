import math

# a fuction to calculate areas of circle,rectangle and triangle 
def calculate_area(shape,dimension1,dimension2=0):
    match shape:
        case "circle":
            return math.pi * dimension1**2
        case "rectangle":
            return dimension1 * dimension2
        case "triangle":
            return 0.5*dimension1*dimension2

        case _:
            return "Invalid shape"

#  function calls to test different shapes and prints the results.
      
print('Circle: {}'.format(calculate_area("circle", 7)))
print('Rectangle:{}'.format(calculate_area("rectangle",12,5)))
print('Triangle: {}'.format(calculate_area("triangle", 8, 4)))
print('Others:{}'.format(calculate_area("oval",9)))
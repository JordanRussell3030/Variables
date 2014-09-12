#Jordan Russell
#variable improvement exercise
#12/09/14

import math

circle_radius = int(input("please enter the radius of the circle: "))

circumference = (2* math.pi * circle_radius)
rounded_circumference = round(circumference, 2)

area = (math.pi * circle_radius**2)
rounded_area = round(area, 2)

print("The circumference of this circle is {0}.".format(circumference))
print("The area of this circle is {0}.".format(area))

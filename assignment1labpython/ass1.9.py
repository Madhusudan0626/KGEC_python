'''Write a program that prompts the user to input the length and the width of a
rectangle and outputs the area and circumference of the rectangle. The formula
is
Area = Length x Width
Circumference = 2 x (Length + Width)'''

# x , y = [float(x) for x in input("Enter the value length and breadth of rectangle\n").split( )]
# area = x * y
# print("Area of the rectangle ",area)

import math as m
r = float(input("Enter the radius of circle \n"))
area = m.pi*r**2
print("Area of circle : ",area)
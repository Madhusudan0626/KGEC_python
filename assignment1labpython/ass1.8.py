'''Write a program that prompts the user to input the radius of a circle and outputs
the area and circumference of the circle. The formula is
Area = pi x radius2
Circumference = 2 x pi x radius
'''
import math as m

r = float(input("Enter the value of the radius \n"))

area = m.pi*r**2
circum = 2*m.pi*r
print("Area of the circle ",area,' Circumference of circle ',circum)
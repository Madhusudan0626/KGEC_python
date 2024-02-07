'''Two numbers are entered through the keyboard. Write a program to find the value of one
number raised to the power of another.'''

x , y =[int(i) for i in input("Enter two numbers\n").split()]

print("y raised to the power of x i.e",x,"^",y,"=",x**y)
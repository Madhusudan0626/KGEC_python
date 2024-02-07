'''Write a program that prompts the user to enter number in two variables and
swap the contents of the variables. (Do not declare extra variable.)
'''
x , y = [float(x) for x in input("Enter the two variables\n").split( )]
print('before swaping ',x,y)

y , x = x , y;

print('after swaping ',x,y)
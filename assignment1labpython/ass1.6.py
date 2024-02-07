'''Write a program that prompts the user to enter number in two variables and
swap the contents of the variables'''

x , y = [float(x) for x in input("Enter the two variables\n").split( )]
print('before swaping ',x,y)

t=x;
x=y;
y=t;

print('after swaping ',x,y)
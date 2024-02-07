'''Write a recursive function that accepts two numbers as its argument and returns its
power.'''

def power_of(x,y):
    if y==0:
        return 1
    y-=1
    return x*power_of(x,y)

x,y=[int(i) for i in input("Enter the number and the power value\n").split()]

print(x,"^",y,"=",power_of(x,y))
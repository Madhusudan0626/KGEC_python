'''Write a program that reads two integers from keyboard and calculate the greatest
common divisor (gcd) using recursive function.'''

def gcd_pro(a,b):
    if a==0:
        return b
    return gcd_pro(b%a,a)

a,b=[int(i) for i in input("Enter two integer\n").split()]

print("GCD of",a,"and",b,"is",gcd_pro(a,b))
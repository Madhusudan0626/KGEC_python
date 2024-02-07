'''Write a program that prompts the user to input two numbers and display its HCF. The
Highest Common Factor (HCF) also called the Greatest Common Divisor (GCD) of two
whole numbers, is the largest whole number that's a factor of both of them.'''

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x%y)

try:
    x , y =[int(x) for x in input("Enter two number\n").split()]
    print("GCD of",x,"and",y,"is",gcd(x,y))

except:
    print("Invalid")
'''Write a program that prompts the user to input a number and prints its factorial. The
factorial of an integer n is defined as n! = 1 x 2 x 3 x ... x n; if n > 0 = 1; if n = 0 For instance,
6! can be calculated as 1 x 2 x 3 x 4 x 5 x 6.'''

def fact(x):
    if x==0:return 1
    return x*fact(x-1)

x=int(input("Enter the number\n"))
print("Factorial of",x,"is",fact(x))
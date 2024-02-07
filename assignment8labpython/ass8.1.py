'''Write a recursive function that accepts an integer argument and returns the factorial.'''

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

x=int(input("Enter the integer : \n"))
print("Factorial of",x,"is",fact(x))
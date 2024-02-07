'''Write a recursive function that accepts a decimal integer and display its binary
equivalent.'''

def d2b(n):
    if n>=1:
        d2b(n//2)#5 2 1 0
    if n!=0:
        print(n%2,end=" ")
    return ""

x=int(input("Enter the decimal number\n"))
print("is Binary equivalent of",x,d2b(x))
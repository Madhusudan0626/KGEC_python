'''Write a program that prompts the user to input a decimal integer and display its binary
equivalent.'''

def decimal_to_binary(n):
    t=n
    b=0
    k=1
    while t>0:
        d=t%2
        b=b+d*k
        k*=10
        t//=2
    print("Binary equivalent ",b)

try:
    x=int(input("Enter the decimal number\n"))
    decimal_to_binary(x)
except:
    print("Invalid input")
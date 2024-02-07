'''Write a program that prompts the user to input a binary number and display its decimal
equivalent.'''

def binary_to_decimal(n):
    t=n
    sum =0
    k=0
    while t>0:
        d=t%10
        sum = sum + d*(2**k)
        k+=1
        t//=10
    print("Decimal equivalent of the number",sum)

try:
    x=int(input("Enter the binary number\n"))
    binary_to_decimal(x)
except:
    print("Invalid input")
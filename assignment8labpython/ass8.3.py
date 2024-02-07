'''Write a recursive function that accepts a number as its argument and returns the sum
of digits'''

def sum_dig(n):
    if n==0:
        return n
    return (n%10)+sum_dig(n//10)

n=int(input("Enter the number\n"))
print("Sum of the digit of",n,"is",sum_dig(n))
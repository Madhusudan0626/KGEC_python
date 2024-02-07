'''Write a recursive function that calculate sum of first n natural numbers.'''

def sum_of_nat(n):
    if n==0:
        return 0
    return n+sum_of_nat(n-1)

x=int(input("Enter the range\n"))

print("Sum of the",x,"th natural numbers is",sum_of_nat(x))
'''Write a program to add first seven terms of the following series using a for loop:'''

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def series():
    sum=0
    for i in range(1,8):
        sum=sum+(1/fact(i))
    return sum

print("sum of 1/1! + 2/2! +......+7/7! is",series())
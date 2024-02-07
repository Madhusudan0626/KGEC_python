'''An Armstrong number of three digits is an integer such that the sum of the cubes of its
digits is equal to the number itself. For example, 371 is an Armstrong number since 33 +
73 + 13 = 371. Write a program to find all Armstrong number in the range of 0 and 999'''

def isarmstrong():
    
    for i in range(0,1000):
        t=i
        sum=0
        while t > 0:
            d=t%10
            sum=sum+d**3
            t//=10
        if sum == i:
            print(sum,end=" ")
    print()

print("Armstrong numbers btw (0,999)")
isarmstrong()

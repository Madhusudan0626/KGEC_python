'''Compute the sum up to n terms in the series'''

def series(n):
    sign=1
    sum=0
    for i in range(1,n+1):
        sum=sum+(sign*(1/i))
        sign*=-1
    print("1-1/2+1/3+...... =",sum)

x=int(input("Enter the positive integer\n"))

if x>0:
    series(x)
else:
    print("Not positive")
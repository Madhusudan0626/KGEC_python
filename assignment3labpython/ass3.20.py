'''Write a program to compute sin x for given x. The user should supply x and a positive
integer n. We compute the sine of x using the series and the computation should use all
terms in the series up through the term involving x n'''

def sinseries(x,n):
    sum=0
    inc=1
    sign=1
    for i in range(1,n+1):
        sum = sum + ((x**inc)/inc)*sign
        sign*=-1
        inc+=2
    print("sum of sin series up to",n,"is",sum)


x , n =[int(i) for i in input("Enter the s in sin x and the range n\n").split()]
sinseries(x,n)
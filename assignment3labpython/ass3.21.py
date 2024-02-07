'''Write a program to compute cosine of x. The user should supply x and a positive integer
n. We compute the cosine of x using the series and the computation should use all terms
in the series up through the term involving x n'''

def sinseries(x,n):
    sum=1
    inc=2
    sign=-1
    for i in range(2,n+1):
        sum = sum + ((x**inc)/inc)*sign
        sign*=-1
        inc+=2
    print("sum of cos series up to",n,"is",sum)


x , n =[int(i) for i in input("Enter the s in sin x and the range n\n").split()]
sinseries(x,n)
'''Write a program that rotates the element of a list so that the element at the first index
moves to the second index, the element in the second index moves to the third index,
etc., and the element in the last index moves to the first index.'''

l=[20,-98,72,0,-1]
print("Before",l)
m=[]
n=[]
for i in range(len(l)-1):
    m.extend(l[i+1:])
    m.extend(l[:i+1])
    n=m
    m=[]
print("After",n)
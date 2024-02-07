'''Write a program to print all elements in a list those have only single occurrence.'''

l=[7, 5, 5, 1, 6, 7, 8, 7, 6]
d=dict()
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

for i in d:
    if d[i]==1:
        print(i,end=" ")
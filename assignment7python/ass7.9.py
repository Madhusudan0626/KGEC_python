'''Write a function half_and_half that takes in a list and change the list such that the
elements of the second half are now in the first half'''

def half_and_half(l):
    n=len(l)
    ml=list()
    if n%2==0:
        h=n//2
        ml+=(l[h:])
        ml+=(l[:h])
    else:
        h=n//2
        ml+=(l[h+1:])
        ml+=(l[:h])
        ml.insert(h,l[h])
    print(ml)

l=[10,20,30,40,50,60,70]
half_and_half(l)

l=[10,20,30,50,60,70]
half_and_half(l)
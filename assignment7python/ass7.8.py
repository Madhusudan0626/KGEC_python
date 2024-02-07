'''For a given list of values in descending order, write a method in python to search for a
value with the help of Binary Search method. The method should return position of the
value and should return -1 if the value not present in the list.'''

def binarysearch(l,val):
    n=len(l)-1
    r=0
    while(r<=n):
        mid = (n+r)//2
        if l[mid]==val:
            return mid
        
        if l[mid]<val:
            r=mid+1
        else:
            n=mid-1
    return -1

ls=[81,64,51,28,23,0]
print("The list ",ls)
ls.sort()
print("sorting into asccending order",ls)
print("Enter the value to be searched")
val=int(input())
get=binarysearch(ls,val)
if  get==-1:
    print("return",get,"not in list")
else:
    print(val,"found at index ",get)
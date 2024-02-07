'''Write a Recursive function in python BinarySearch(Arr, L, R, X) to search the given
element X to be searched from the List Arr having R elements, where L represents lower
bound and R represents the upper bound.'''

def BinarySearch(Arr, L, R, X):
    
    if L>R:
        print("Not found")
        return
    mid=(L+R)//2

    if X==Arr[mid]:
        print("Found it! at index",mid)
        return True
    
    if X>Arr[mid]:
        BinarySearch(Arr,mid+1,R,X)
    else:
        BinarySearch(Arr,L,mid-1,X)
l=[int(i) for i in input("Enter elements to the list\n").split()]
l.sort()
print("The sorted list",l)
x=int(input("Enter the element to be searched\n"))
BinarySearch(l,0,len(l)-1,x)

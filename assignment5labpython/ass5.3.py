''' Find and display the largest number of a list without using built-in function max(). Your
program should ask the user to input values in list from keyboard.'''
import sys
mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter',str(size),'elements')

for i in range(size):
    data = int(input())
    mylist.append(data)
m=-sys.maxsize-1

for i in range(len(mylist)):
    if mylist[i]>m:
        m=mylist[i]
print("Maximum",m)
    
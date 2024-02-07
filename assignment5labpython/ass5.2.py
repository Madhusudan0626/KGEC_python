'''Write a program that accepts a list from user. Your program should reverse the content
of list and display it. Do not use reverse() method'''

mylist = []
size = int(input('How many elements you want to enter? '))

print('Enter',str(size),'elements')

for i in range(size):
    data = int(input())
    mylist.append(data)

print("Reverse")
print(mylist[::-1])
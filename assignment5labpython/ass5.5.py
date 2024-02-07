'''Write a program that input a string and ask user to delete a given word from a string.'''

s=input("Enter the string\n")
temp=s.split()
c=input("Enter the word to be deleted\n")
flag=0
for i in s.split():
    if i==c:
        temp.remove(c)
        flag=1
        break

if flag:
    print(" ".join(temp))
else:
    print("Not found")




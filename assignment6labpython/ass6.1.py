'''Write a program that reads a string from keyboard and prints the unique words. Your
program should convert input string to lower case.'''

x=input("Enter the string\n")
s=x.lower()
d=dict()
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

for key,value in d.items():
    if value==1:
        print(key,end=" ")
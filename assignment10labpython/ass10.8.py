'''Write a function in Python to count uppercase character in a text file.'''
import re
f=open("story.txt")
reg="[A-Z]"
count=0
for i in f:
    make=re.findall(reg,i)
    count+=len(make)

f.close()
print("Number of uppercase character",count)
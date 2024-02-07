'''Write a function in Python to count the words "this" and "these" present in a text file
"article.txt"'''
import re
f=open("article.txt","r")
count=0
reg="[T|t]hese|[T|t]his"
i=f.read()
make=re.findall(reg,i)
count+=len(make)
print("Number of \"this\" and \"these\"",count)
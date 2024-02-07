'''Write a function in Python to count words in a text file those are ending with alphabet
"e".'''

import re
f=open("story.txt","r")

reg="(e)[^a-zA-Z]"
count=0
i=f.read()
make=re.findall(reg,i)
count+=len(make)

f.close()
print(count,"Number of words in a \"story.txt\" those are ending with alphabet \"e\"")
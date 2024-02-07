'''Write a function in python to count the number of lines from a text file "story.txt" which
is not starting with an alphabet "T"'''

f=open("story.txt","r")
count=0
for i in f:
    if i.split()[0][0] !='T':
        count+=1

print("Number of lines not starting with \"T\"",count)
f.close()
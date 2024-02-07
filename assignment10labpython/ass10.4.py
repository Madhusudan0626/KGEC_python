'''Write a function in Python to read lines from a text file "notes.txt". Your function should
find and display the occurrence of the word "the"'''

f=open("poem.txt","r")
count=0
for i in f:
    if "the" in i.split():
        count+=1
print("The occurrence of the word \"the\"",count)
f.close()
'''Write a function in python to read the content from a text file "poem.txt" line by line and
display the same on screen.'''

f=open("poem.txt","r")
i=f.read()
print(i)
f.close()
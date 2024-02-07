'''Write a function in Python to count and display the total number of words in a text file.'''

f=open("story.txt","r")
i=f.read().split()
print("Total Number of words - ",len(i))
f.close()
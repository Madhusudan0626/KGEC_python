'''Write a function display_words() in python to read lines from a text file "story.txt", and
display those words, which are less than 4 characters.'''

def display_words(f):
    m=f.read()
    m1=m.split()
    for j in m1:
        if len(j)<4:
            print(j,end=" ")

f=open("story.txt","r")
display_words(f)
f.close()


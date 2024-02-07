'''Assume that a file 'names.txt' containing a series of names (as strings) exists on the
computer’s disk. Write a function, first_five() that displays only the first five lines of the
file’s contents. If the file contains less than five lines, it should display the file’s entire
contents.'''

def first_five(f):
    j=0
    flag=0
    for i in f:
        if j>4:
            break
        j+=1
        print(i)
    if j<5:
        for i in f:
            print(i)
f=open("notes.txt","r")

first_five(f)

f.close()
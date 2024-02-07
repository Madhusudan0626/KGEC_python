'''A text file named "matter.txt" contains some text, which needs to be displayed such that
every next character is separated by a symbol "#". Write a function definition for hash_display() 
in Python that would display the entire content of the file matter.txt in
the desired format.'''

def hash_display(f):
    data=f.read()
    print(data)
    for i in data:
        if i.isalpha():
            print(i,end="#")

f=open("matter.txt","r")

hash_display(f)
f.close()
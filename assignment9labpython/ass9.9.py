'''Write the definition of a Python function named long_lines( ) which reads the contents
of a text file named 'lines.txt' and displays those lines from the file which have at least 8
words in it'''

def long_lines(f):
    l=list(f)
    for i in l:
        m=i.split()
        if len(m)>7:
            print(i)

f=open("lines.txt","r")

long_lines(f)

f.close()
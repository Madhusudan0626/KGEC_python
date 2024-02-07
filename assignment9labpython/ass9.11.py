'''Create a Python function make_copy() that reads a text file 'input.txt' and writes its
contents to a new file 'output.txt', capitalizing the first letter of each word.'''

def make_copy(f):
    fw=open("ouput.txt","+x")
    for i in f:
        fw.write(i)
    print("Copied!")

f=open("input.txt","r")
make_copy(f)

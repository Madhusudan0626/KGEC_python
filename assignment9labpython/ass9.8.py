'''Write a Python program that reads a text file and prints its contents in reverse order'''

f=open("zen.txt","r")
f1=list(f)
for i in f1[::-1]:
    j=(i.split()[::-1])
    print(" ".join(j))
f.close()
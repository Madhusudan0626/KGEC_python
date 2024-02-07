'''Write a function last_digit_words() in Python to count the words ending with a digit in a
text file "notes.txt"'''

def last_digit_words(f):
    count=0
    for i in f:
        m=i.split()
        for j in m:
            if j[-1:].isnumeric():
                count+=1
                print(j)
    print("Number of words ending with a digit are",count)

f=open("notes.txt","r")
last_digit_words(f)


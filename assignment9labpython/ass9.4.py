'''Write a function lines_count() that reads lines from a text file named 'zen.txt' and
displays the lines that begin with any vowel. Assume the file contains the following text
and already exists on the computer's disk:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.'''

def lines_count(f):
    s="aeiouAEIOU"
    for i in f:
        if i[0] in s:
            print(i)

f = open("zen.txt","r")
print(lines_count(f))

f.close()
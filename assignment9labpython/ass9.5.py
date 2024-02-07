'''Assume that the file 'notes.txt' containing some text and exists on the computer’s disk.
Write a program that display only those words from 'notes.txt' file whose length is more
than seven. Keep in mind that any punctuation marks at the beginning or end of a word
should also be considered as part of the word's length.'''

f = open("notes.txt","r")
print("only those words from 'notes.txt' file whose length is more than seven")
for i in f:
    for j in range(len(i.split())):
        if len(i.split()[j])>7:
            print(i.split()[j],end=" ")

f.close()
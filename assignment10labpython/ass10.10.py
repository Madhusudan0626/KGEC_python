'''Aditi has used a text editing software to type some text. After saving the article as
WORDS.TXT, she realised that she has wrongly typed alphabet J in place of alphabet I
everywhere in the article.
Write a function definition for JTOI() in Python that would display the corrected version
of entire content of the file WORDS.TXT with all the alphabets "J" to be displayed as an
alphabet "I" on screen.'''


def JTOI(f):
    d=f.read()

    for i in d:
        if i=="J":
            print("I",end="")
        else:
            print(i,end="")
f=open("words.txt","r")
JTOI(f)
f.close()


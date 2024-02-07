'''Write a function AMCount() in Python, which should read each character of a text file
STORY.TXT, should count and display the occurance of alphabets A and M (including small
cases a and m too).'''

def AMCount(F):
    i=f.read()
    count1=count2=0
    for j in i:
        if j is "a" or j is "A":
            count1+=1
        elif j is "m" or j is "M":
            count2+=1
    print("A or a:",count1,"\nM or m:",count2)

f=open("story.txt","r")

AMCount(f)
f.close()
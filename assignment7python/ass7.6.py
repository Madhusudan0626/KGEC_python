'''Write a definition of a method count_now(places) to find and display those place names,
in which there are more than 5 characters.'''
import re
def count_now(l):
    ap=[]
    for i in l:
        if len(i)>5:
            ap.append(i)
    print("place's naem having more than 5 character \n",[x for x in ap])



l=[x for x in input("Enter the name of the city\n").split("\t")]
count_now(l)

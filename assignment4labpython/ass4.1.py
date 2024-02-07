'''Write a program that accepts a string from user. Your program should count and display
number of vowels in that string.'''

l="aeiouAEIOU"
d=dict()
x=input("Enter the string\n")

for c in x:
    if c in l:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1

print("Number of vowels : ")
for key in d:
    print(key,"->",d[key])
'''Write a Python program that accepts a string from user. Your program should create a new
string by shifting one position to left.
For example if the user enters the string 'examination 2021' then new string would be
'xamination 2021e'''

x=input("Enter the string\n")

t=list(x)

t.append(x[0])
t.pop(0)
print("New string shifting one position to left","".join(t))
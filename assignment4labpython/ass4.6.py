'''Write a program that asks the user to input his name and print its initials. Assuming that the
user always types first name, middle name and last name and does not include any
unnecessary spaces.
For example, if the user enters Ajay Kumar Garg the program should display A. K.G.
Note: Don't use split() method'''

x = input("Enter the name\n")
m=""
m+=x[0]
m+='.'
for i in range(len(x)):
    if x[i] ==' ':
        m+=x[i+1]
        m+='.'
print(m.upper())
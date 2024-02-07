'''Write a program that prompts the user to input a number and reverse its digits. For
example, the reverse of 12345 is 54321; reverse of 5600 is 65.'''

x=int(input("Enter the number\n"))

t=x
k=10
rev=0
while t>0:
    d=t%10
    rev=rev*k+d
    t=t//10
print("Reverse of a digits",rev)


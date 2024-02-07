'''Write a Python program that accepts a string from user. Your program should create and
display a new string where the first and last characters have been exchanged.
For example if the user enters the string 'HELLO' then new string would be
'OELLH'''

x=input("Enter the string\n")
t=list(x)
j=""
t[0] , t[-1] = t[-1] , t[0] 
j=j.join(t)
print("First and last characters have been exchanged ",j)
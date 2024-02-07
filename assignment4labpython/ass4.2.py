'''Write a program that reads a string from keyboard and display:
 The number of uppercase letters in the string
 The number of lowercase letters in the string
 The number of digits in the string
 The number of whitespace characters in the string'''

x=input("Enter the string\n")
upper = lower = number = symbol = 0
for c in x:
    if c.isupper():
        upper+=1
    elif c.islower():
        lower+=1
    elif c.isnumeric():
        number+=1
    else:
        symbol+=1
print("Uppercase : ",upper,"\nLowercase : ",lower,"\nNumber : ",number,"\nSymbol : ",symbol)

'''Write a program that prompts the user to input two integers and outputs the largest.'''

try:
    x , y = [int(i) for i in input("Enter two integers\n").split( )]
    if x > y :print(x , " is largest\n")
    else:print(y , " is largest\n")
except:
    print("Invalid datatype..\n")
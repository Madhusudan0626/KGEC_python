'''Write a program that prompts the user to input three integers and outputs the largest.'''

try:
    x , y , z= [int(i) for i in input("Enter three integers\n").split( )]
    if x > y :
        if x > z:
            print(x , "is largest\n")
        else:
            print(z , "is largest\n")
    else:
        if y > z:
            print(y , "is largest\n")
        else:
            print(z , "is largest\n")

except:
    print("Invalid datatype..\n")
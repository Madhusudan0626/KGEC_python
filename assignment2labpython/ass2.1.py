'''Write a program that prompts the user to input a number and display if the number is even or
odd.'''
try:
    x = int(input("Enter the integer \n"))
    if(x<0):
        x=-x    
    if x % 2 == 0:
        print("Number is even...\n")
    elif x % 2 != 0:
        print("Number is odd...\n")
    else:
        print("Number is zero\n")
except:
    print("invalid data type")
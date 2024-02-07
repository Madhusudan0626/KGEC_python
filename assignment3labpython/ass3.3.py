'''Write a program that prompts the user to input a number and prints its mulitiplication table.'''

try:
    x=int(input("Enter the number\n"))
    for i in range(1,11):
        print(x ,"x",i,"=",x*i)
except:
    print("Invalid output")
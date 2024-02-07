'''Write a program to enter the numbers till the user wants and at the end the program
should display the largest and smallest numbers entered.'''

d=list()
try:
    while(True):
        x=input("Enter the number wirte exit for exit\n")
        if x=="exit":
            break
        else:
            d.append(x)
    print(d)
    print("Maximum is :",max(d),"Minimum is :",min(d))
except:
    print("Invalid input")
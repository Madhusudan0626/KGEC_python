'''Write a program to enter the numbers till the user wants and at the end it should display
the count of positive, negative and zeros entered.'''

def count(d,n):

    if n not in d:
        d[n]=1
    else:
        d[n]+=1


d=dict()
try:
    while(True):
        x=input("Enter the number wirte exit for exit\n")
        if x=="exit":
            break
        else:
            count(d,int(x))
    print(d)
except:
    print("Invalid input")
    
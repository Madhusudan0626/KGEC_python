'''Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
Dictionary's value should be stored in list'''

def addtodic():
    d=dict()
    odd=[]
    even=[]
    for i in range(6):
        x=int(input("Enter any integer\n"))
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    d["Even"]=sorted(odd)
    d["Odd"]=sorted(even)
    print(d)
                
addtodic()

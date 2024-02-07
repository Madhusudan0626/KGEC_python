'''Write a program to enter names of employees and their salaries as input and store them
in a dictionary.'''

def inputdic():
    d=dict()
    while True:
        x=input("Enter the name(enter \"exit\"for exit)\n")
        if x == "exit":
            print(d)
            break
        f=float(input("Enter the salary\n"))
        d[x]=f     

inputdic()





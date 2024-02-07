'''Write a program that display following output:
SHIFT
HIFTS
IFTSH
FTSHI
TSHIF
SHIFT'''
x = input("Enter the string\n")

t=""
for i in range(len(x)):
    c=x[i+1:]
    t=c+x[:i+1]
    print(t)

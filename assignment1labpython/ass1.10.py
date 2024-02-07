import math as m

def validity(a,b,c):
    if a+b <= c or b+c <= a or a+c <= b:
        return False
    else:
        return True

a , b ,c =[float(x) for x in input("Enter the length , width and height of triangle\n").split( )]
if(validity(a,b,c)):

    s=(a+b+c)/2
    area = m.sqrt(s*(s-a)*(s-b)*(s-c))

    print('Area of triangle ',area)
else:
    print("Not a valid Triangle")
'''The roots of the quadratic equation ax2 + bx + c = 0, a ≠ 0 are given by the following formula:
In this formula, the term b2 - 4ac is called the discriminant. If b2 - 4ac = 0, then the equation 
has two equal roots.
If b2 - 4ac > 0, the equation has two real roots. If b2 - 4ac < 0, the equation has two complex 
roots. 
Write a program that prompts the user to input the value of a (the coefficient of x2),
b (the coefficient of x), and c (the constant term) and outputs the roots of the quadratic equation.'''
try:
    t=int(input("Enter the marks - \n"))
    if t >= 90 and t <= 100:
        print("Grade A")
    elif t >= 80 and t <= 89:
        print("Grade B")
    elif t>=70 and t<=79:
        print("Grade C")
    elif t>=60 and t<=69:
        print("Grade D")
    elif t>=0 and t<=59:
        print("Grade F")
except:
    print("Inavild Datatype")
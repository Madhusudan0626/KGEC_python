try:
    a , b , c = [int(x) for x in input("Enter the coefficent of x^2 ,the coefficient of x , c (the constant term)\n").split( )]
    d=b**2 - 4*a*c

    if d < 0:
        print("Equation has two complex roots.")
    elif d > 0:
        print("Equation has two real roots.")
    else:
        print("Equation has two equal roots")

except:
    print("Inavlid input datatype")

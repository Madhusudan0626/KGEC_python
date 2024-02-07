'''Write a program that asks the user to input a positive integer. Your program should find
and display the sum of digits of number. For example, sum of digits of number 32518 is
3+2+5+1+8 = 19.'''

try:
    x=int(input("Enter the number\n"))
    sum=0
    t=x
    while t>0:
        d=t%10
        if d != 0:
            sum+=d
        t//=10
    print("Sum of the digits ",sum)
except:
    print("Invalid input")

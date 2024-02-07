'''Write a program that asks the user for a positive integer value. The program should
calculate the sum of all the integers from 1 up to the number entered. For example, if the
user enters 20, the loop will find the sum of 1, 2, 3, 4, ... 20.'''


sum = 0
try:
    x=int(input("Enter the positive integer\n"))
    if x<0:
        print("Enter positive integer")
    else:
        for i in range(0,x+1):
            sum+=i
        print("Sum is : ",sum)
except:
    print("Invalid")
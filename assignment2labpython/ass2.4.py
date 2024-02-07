'''Write a program that prompts the user to input a year and determine whether the year is a
leap year or not.Leap Years are any year that can be evenly divided by 4. A year that is evenly divisible by 100
is a leap year only if it is also evenly divisible by 400. Example:
1992
2000
1900
1995
Leap Year
Leap Year
NOT a Leap Year
NOT a Leap Year'''

try:
    x = int(input("Enter the value of year \n"))
    
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print("Leap year")
    else:
        print("Not a Leap year")
except:
    print("invalid input datatype")
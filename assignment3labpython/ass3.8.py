'''A palindromic number is a number that remains the same when its digits are reversed.
For example, 16461. Write a program that prompts the user to input a number and
determine whether the number is palindrome or not.'''

def check_palindrome(n):
    t=n
    rev=0
    k=10
    while(t>0):
        d=t%10
        rev=rev*k+d
        t//=10
    if rev == n:
        return True
    return False
try:
    x=int(input("Enter the number\n"))
    if check_palindrome(x):
        print(x,"is palindrome")
    else:
        print(x,"is not palindrome")
except:
    print("Invalid numer")
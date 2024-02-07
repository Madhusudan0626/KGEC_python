'''A palindrome is a string that reads the same backward as forward. For example, the words
dad, madam and radar are all palindromes. Write a programs that determines whether the
string is a palindrome.
Note: do not use reverse() method'''

x = input("Enter the string\n")
n=len(x)
flag = 0
for i in range(len(x)//2):
    if x[i] != x[n-i-1]:
        print("string is not palindrome")
        flag=0
        break
    else:
        flag =1

if flag :
    print("string is palindrome")
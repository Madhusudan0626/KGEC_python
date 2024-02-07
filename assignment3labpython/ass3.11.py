'''Write a program that prompts the user to input a positive integer. It should then output a
message indicating whether the number is a prime number. A prime number is a number
that is evenly divisible only by itself and 1. For example, the number 5 is prime because
it can be evenly divided only by 1 and 5. The number 6, however, is not prime because it
can be divided evenly by 1, 2, 3, and 6'''

def ispirme(n):
    if n is 2:
        return True
    else:
        i=3
        while i<n:
            if n % i == 0:
                break
            i+=2
        if n==i:
            return True
        return False

try:
    x=int(input("Enter the integer\n"))

    if x > 0:
        if ispirme(x):
            print(x,"is prime number")
        else:
            print(x,"is not prime number")
    else:
        print("Negative...")
except:
    print("Invalid")
'''Write a recursive function that accepts an integer argument in n. This function returns
the nth Fibonacci number. Call the function to print fibonacci sequences.'''

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

x=int(input("Enter the number\n"))
print(x,"th fibonacci number is(counting from 0 ,1 ,...)",fib(x-1))
    
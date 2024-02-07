'''Write a program to obtain the first 25 numbers of a Fibonacci sequence. In a Fibonacci
sequence the sum of two successive terms gives the third term. Following are the first
few terms of the Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34 55 89...'''

def fibseries():
    h1=0
    h2=1
    print(h1,h2,end=" ")
    for i in range(1,24): 
        h3=h1+h2
        h1=h2
        h2=h3
        print(h3,end=" ")
print("Fibonacci series for first 25 number")
fibseries()
print()
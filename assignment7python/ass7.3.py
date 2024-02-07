'''Write a function named is_prime, which takes an integer as an argument and returns true
if the argument is a prime number, or false otherwise. Also, write the main function that
displays prime numbers between 1 to 500.'''
def is_prime(c):
    flag=0
    for i in range(3,500,2):
        if c%i==0:
            break
    
    if i==c:
        return True
    else:
        return False
    
def main():
    d=[]
    d.append(2)
    for i in range(3,500,2):
        if is_prime(i):
            d.append(i)
    
    print(d)
    
if __name__ == "__main__":
    main()

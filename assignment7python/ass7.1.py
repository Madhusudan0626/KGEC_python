'''Write a function find_max that accepts three numbers as arguments and returns the
largest number among three. Write another function main, in main() function accept
three numbers from user and call find_max.'''

def find_max(a,b,c):
    return max(a,b,c)
def main():
    a,b,c =[int(x) for x in input("Enter three number\n").split()]
    print("Max is ",find_max(a,b,c))
if __name__ == '__main__':
    main()

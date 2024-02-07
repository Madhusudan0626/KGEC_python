'''Write a function in python to find the sum of the cube of elements in a list. The list is
received as an argument to the function, in turn, the function must return the sum. Write
the main function which invokes the above function'''

def sum_cube(l):
    return sum([x**3 for x in l])

def main():
    s=[int(x) for x in input("Enter the elements of the list\n").split()]
    print("sum of the cube of elements ",sum_cube(s))
    pass
    
if __name__ == "__main__":
    main()

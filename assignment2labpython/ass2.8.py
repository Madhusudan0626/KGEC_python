l = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

try:
    x = int(input("Enter a number\n"))
    print("It's",l[x-1])
except:
    print("list out of index...\n")
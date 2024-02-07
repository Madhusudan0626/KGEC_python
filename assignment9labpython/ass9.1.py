'''Write a program that writes 10 random numbers to a file 'numbers.txt'. Each random
number should be in the range of 1 through 100.'''

import random as ra
f=open("random.txt","w")
for i in range(1,10):
    f.write(str(ra.randint(1,100)))
    f.write("\n")
print("Done!")
f.close()
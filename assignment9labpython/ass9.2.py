'''Write a program that reads and display all of the numbers stored in the file numbers.txt
(created in question 1) and calculates their total.'''

f=open("random.txt","r")
sum=0
for i in f:
    print(i,end="")
    sum=sum+int(i)

print("Sum of the number stored in the file created in question 1 is",sum)
f.close()
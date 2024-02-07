'''Write a program that accepts seconds from keyboard as integer. Your program
should convert seconds in hours, minutes and seconds. Your output should like
this:
Enter seconds: 13400
Hours: 3
Minutes: 43
Seconds: 20
'''

s=int(input("Enter the value of second "))
h=s//3600;
m=s%3600;
min=m//60;
sec=m%60

print("Hours : ",h)
print("Minutes : ",min)
print("Second : ",sec)


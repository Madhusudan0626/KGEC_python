'''A binary file "STUDENT.DAT" has structure (admission_number, Name, Percentage).
Write a function count_rec() in Python that would read contents of the file"STUDENT.DAT" and display the details of those students whose percentage is above 75.
Also display number of students scoring above 75%'''

import sys
import pickle
def createFile():
    file = open("student.dat","ab")
    admission_number = int(input("\nEnter date of admission(enter \'0\' for exit): "))
    Name = input("Enter student Name: ")
    Percentage = float(input("Enter percentage: "))
    record = [admission_number, Name, Percentage]
    pickle.dump(record, file)
    file.close()

def count_rec():
    file = open("student.dat","rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            if record[2] > 75:
                print(record)
                count+=1
    except EOFError:
        pass
    print('No of students having more than 75% are', count)
    file.close()

while(1):
    print("1. Add data\n2. Percentages > 75%\n3. Exit")
    x=input("Enter choice\n")
    if x=="1":
        createFile()
    elif x=="2":
        count_rec()
    elif x=="3":
        sys.exit()
    else:
        print("Wrong choice")

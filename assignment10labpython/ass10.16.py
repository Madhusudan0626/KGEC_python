'''A binary file school.dat has structure(rollno, name, class, fees)
Write a definition for function total_fees( ) that reads each object of file and calculate
the total fees of students and display the same.'''

import pickle
import sys
def insert_record():
    file = open("school.dat","ab")
    try:
        rollno=int(input("Enter rollno\n"))
        name = input("Enter name of student\n")
        class_name=input("Enter class\n")
        fees=float(input("Enter fees\n"))
        add=[rollno,name,class_name,fees]
        pickle.dump(add,file)
    except EOFError:
        pass
    file.close()

def total_fees():
    file = open("school.dat","rb")
    try:
        total = 0
        while True:
            record = pickle.load(file)
            total += record[3]
    except EOFError:
        pass
    print('Total Fees: ',total)
    file.close()

def show():
    file = open("school.dat","rb")
    try:
        while True:
            record = pickle.load(file)
            print(record)
    except:
        pass

while True:
    print("1. Add record\n2. Total Fess\n3. Show \n4.Exit")
    x=int(input("Enter your choice\n"))

    if x==1:
        insert_record()
    elif x==2:
        total_fees()
    elif x==3:
        show()
    elif x==4:
        sys.exit()
    else:
        print("Invalid option")
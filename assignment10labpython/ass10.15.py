'''Write a function to search and display details of student whose rollno is '1005' from the
binary file student.dat having structure [rollno, name, class and fees].'''

import pickle
def search():
    file = open("student.dat","rb")
    try:
        while True:
            record = pickle.load(file)
            if record[0] == 1005:
                print(record)
    except EOFError:
        pass
    file.close()
search()

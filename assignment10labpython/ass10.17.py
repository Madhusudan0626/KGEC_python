'''A binary file players.dat, containing records of following list format: [code, name, country
and total runs]
Write a python function that display all records where player name starts from 'A'
Write a python function that accept country as an argument and count and display the
number of players of that country.
Write a python function that add one record at the end of file.'''

import pickle

def createFile():
    file = open("players.dat","ab")
    Code = int(input("Enter player code: "))
    Name = input("Enter player Name: ")
    Country =input("Enter player country: ")
    Total_Runs = int(input("Enter total runs of player: "))
    record = [Code, Name, Country, Total_Runs]
    pickle.dump(record, file)
    file.close()

def search():
    file = open("players.dat","rb")
    count=0
    try:
        while True:
            record = pickle.load(file)
            if record[1][0] == 'A':
                count+=1
                print(record)
    except EOFError:
        pass
    file.close()
    return count

def countRec(Country):
    file = open("players.dat","rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            print(record)
            if record[2]==Country:
                count+=1
    except EOFError:
        pass
    file.close()
    return count
    

def testProgram():
    while True:
        createFile()
        choice = input("Add more record (y/n)? ")
        if choice in 'Nn':
            break
    print("the number of players whose name starts with A:",search())
    Country = input('Enter country name to search: ')
    n = countRec(Country)
    print("No of players are",n)

testProgram()
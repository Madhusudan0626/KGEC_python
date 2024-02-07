'''Given a binary file game.dat, containing records of following list format: [game_name,
participants]
Write a function in Python that would read contents from the file game.dat and creates
a file named basket.dat copying only those records from game.dat where the game name
is "Basket Ball"'''
import pickle
import sys
def create_game_details():
    file = open("game.dat","ab")
    game_name=input("Enter Game Name\n")
    participants=input("Enter participant name\n")
    add=[game_name,participants]
    pickle.dump(add,file)
    file.close()
def show():
    print("Content of game.dat")
    infile=open("game.dat","rb")
    try:
        while True:
            record = pickle.load(infile)
            print(record)
    except EOFError:
        pass

    print("Content of basket.dat")
    infile=open("basket.dat","rb")
    try:
        while True:
            record = pickle.load(infile)
            print(record)
    except EOFError:
        pass
def countRec(country):
    
    infile = open("game.dat","rb")
    outfile = open("basket.dat","wb")
    outfile.seek(0)
    outfile.truncate()
    try:
        while True:
            record = pickle.load(infile)
            if record[0] == "Basket Ball":
                pickle.dump(record, outfile)
                print("Added to basket.dat!!!")
    except EOFError:
        pass
    infile.close()
    outfile.close()

while True:
    print("1. Add record\n2. Search Player Number\n3. Show\n4. Exit")
    x=int(input("Enter choice\n"))

    if x==1:
        create_game_details()
    elif x==2:
        c=input("Enter game Name\n")
        countRec(c)
    elif x==3:
        show()
    elif x==4:
        sys.exit()
    else:
        print("Wrong Choice")
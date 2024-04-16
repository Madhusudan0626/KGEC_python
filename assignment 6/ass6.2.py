#Write a Python program that implements queue as a linked list.
import sys
class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
    def __del__(self):
        print("Destructor")

class Queue(Node):
    def __init__(self):
        self.rear = None
        self.front = None
    
    def isempty(self):
        return self.rear ==None

    def insertInQ(self,data):
        nwnode = Node(data)
        if self.rear == None:
            self.rear = self.front = nwnode 
            return
        self.rear.next = nwnode
        self.rear = nwnode
    

    def deleteFromQ(self):
        if self.front == None:
            print("Queue is empty")
            return
        
        temp=self.front
        self.front = temp.next
        print("Delted item",temp.data)
        del temp
        pass

    def displayQ(self):
        if self.front==None and self.rear == None:
            print("Empty queue")
            return
        temp = self.front
        print("The queue - >")
        while temp:
            print(temp.data)
            temp = temp.next
        pass


if __name__ == "__main__":
    q = Queue()
    print("QUEUE")
    while True:
        print("1.Insert")
        print("2.Delete")
        print("3.Display")
        print("4.Exit")
        print("Enter your choice")
        ch = int(input())

        if ch == 1:
            q.insertInQ(int(input("Enter value : \n")))
        elif ch == 2:
            q.deleteFromQ()
        elif ch == 3:
            q.displayQ()
        elif ch == 4:
            sys.exit()
        else:
            print("Invalid")
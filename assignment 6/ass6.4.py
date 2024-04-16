# Write a Python program that implements deque using a linked list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev = None
    def __del__(self):
        print("Destructor")

class Dqueue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0
    
    def isEmpty(self):
        return self.front == None
    
    def insertFrontend(self,data):
        nwnode = Node(data)
        if nwnode is None:
            print("Overflow")
            return
        if self.front == None:
            self.rear = self.front = nwnode
        else:
            nwnode.next = self.front
            self.front.prev=nwnode
            self.front=nwnode
        pass

    def insertRearend(self,data):
        nwnode = Node(data)
        if nwnode is None:
            print("Overflow")
            return
        if self.rear == None:
            self.rear = self.front = nwnode
        else:
            nwnode.prev = self.rear
            self.rear.next=nwnode
            self.rear=nwnode
        pass

    def deleteFrontEnd(self):
        if self.front == None:
            print("Underflow")
            return
        
        temp = self.front
        self.front = self.front.next

        if self.front == None:
            self.rear = None
            print(temp.data ,"removed")
            del temp
            return
        self.front.prev = None
        print(temp.data ,"removed")
        del temp    
    def deleteRearEnd(self):
        if self.rear == None:
            print("Underflow")
            return
        
        temp = self.rear
        self.rear = self.rear.prev

        if self.rear == None:
            self.front = None
            print(temp.data ,"removed")
            del temp 
            return
        self.rear.next = None
        print(temp.data ,"removed")
        del temp 
        pass

    def getFront(self):
        if self.isEmpty():
            print("empty queue")
            return
        print("Front value",self.front.data)

    def getRear(self):
        if self.isEmpty():
            print("empty queue")
            return
        print("Rear value",self.rear.data)

    def display(self):
        if self.isEmpty():
            print("Empty queue")
            return
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        
        print()

if __name__=="__main__":
    q = Dqueue()
    while True:
        print("1.Insert into Front")
        print("2.Insert into Rear")
        print("3.Delete from Front")
        print("4.Delete from rear")
        print("5.Get Front")
        print("6.Get Rear")
        print("7.Display")
        print("8.Exit")

        print("Enter your choice")
        ch = int(input())

        if ch==1:
            q.insertFrontend(int(input("Enter value\n")))
        elif ch==2:
            q.insertRearend(int(input("Enter value\n")))
        elif ch==3:
            q.deleteFrontEnd()
        elif ch==4:
            q.deleteRearEnd()
        elif ch==5:
            q.getFront()
        elif ch==6:
            q.getRear()
        elif ch==7:
            q.display()
        elif ch==8:
            break
        else:
            print("Invalid choice")



    
    

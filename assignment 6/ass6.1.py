import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __del__(self):
        print("Destruction")


class Stack(Node):
    def __init__(self):
        self.head = None

    def push(self,x):
        nwnode = Node(x)
        if self.head == None:
            self.head = nwnode
            return
        temp = self.head
        self.head = nwnode
        self.head.next = temp

    def pop(self):
        if self.head == None:
            print("Underflow")
            return
        
        temp = self.head
        self.head = temp.next
        print(temp.data ,"deleted.")
        del temp

        pass

    def display(self):
        print("The stack -> ")
        if self.head == None:
            print("Empty stack")
            return
        temp = self.head
        while temp:
            print(temp.data , end = " ")
            temp = temp.next

        print()

if __name__ == "__main__":
    s=Stack()
    print("STACK")
    while True:
        print("1.Push")
        print("2.Pop")
        print("3.Display")
        print("4.Exit")
        print("Enter your choice")
        ch = int(input())

        if ch == 1:
            print("Enter value")
            s.push(int(input()))
        elif ch == 2:
            s.pop()
        elif ch == 3:
            s.display()
        elif ch == 4:
            sys.exit()
        else:
            print("Invalid")


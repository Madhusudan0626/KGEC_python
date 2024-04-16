# Write a python program to create a linked list to contain the vowels ‘a’, ‘e’, ‘i’, ‘o’, ‘u’ in
# the data field of the nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    
    def addNode(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next=newNode
    
    def deletefirst(self):
        if self.head == None:
            print("Linked list is empty")
            return
        if type(self.head.data) == int:
                temp = self.head
                print("Deleted item",temp.data)
                self.head=temp.next

        else:
            print("Not int")
    

    def printList(self):
        if self.head == None:
            print("Empt linked list")
            return
        temp = self.head

        while temp:
            print(temp.data , end= " ")
            temp = temp.next

        print()


if __name__ == "__main__":
    print("Linked list containing vowels : ")
    l = LinkedList()
    l.addNode(54)
    l.addNode('a')
    l.addNode('e')
    l.addNode('i')
    l.addNode('o')
    l.addNode('u')
    
    l.printList()
    l.deletefirst()
    l.printList()


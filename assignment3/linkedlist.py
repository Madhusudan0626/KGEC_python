#Singly Linked List 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __del__(self):
        print("Destroy")
    def swap_two(n1,n2):
        temp= n1.data
        n1.data = n2.data
        n2.data= temp
class SinglyLinkedList(Node):
    def __init__(self):
        self.head = None

    #add a node to linked list
    def addNode_S(self,x):
        newnode=Node(x)
        if self.head is None:
            self.head = newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode

    #Display the list
    def display_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    


    
class Insertion_Deletion(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    #insert at first of linked list
    def insert_first(self,x):
        newnode = Node(x)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        self.head=newnode
        newnode.next=temp

    #insert at last of linked list
    def insert_last(self,x):
        newnode = Node(x)

        if self.head is None:
            self.head = newnode
            return 

        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
    
    #insert into sprcifc position of linked list
    def insert_spec_pos(self,x,pos):
        newnode = Node(x)
        if pos == 1:
            Insertion_Deletion.insert_first(self,x)
            return
        else:
            l=0
            temp=temp1=temp2=self.head
            while temp1:
                temp1=temp1.next
                l+=1
            print("1. After the ",pos," position.\n2. Before the ",pos," position.")
            print("Please specify the position")
            ch = int(input())
            if ch ==1:
                pos +=1
            if pos <= l and pos > 0:
                while pos>1:
                    temp2=temp
                    temp=temp.next
                    pos-=1
                temp2.next=newnode
                newnode.next=temp
            else:
                print("Invalid position")

    #delete first Node
    def delete_first(self):
        if self.head is None:
            print("Empty Linked List")
            return
        
        temp=self.head.next
        self.head=temp

    #delete last Node
    def delete_last(self):
        if self.head is None:
            print("Empty Linked List")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next:
            temp2=temp
            temp=temp.next
        temp2.next=None

    #delete at specific position
    def delete_spec_pos(self,pos):
        if self.head is None:
            print("Empty Linked list")
            return
        if pos==1:
            Insertion_Deletion.delete_first(self)
            return
        l=0
        temp=temp1=temp2=self.head

        while temp1:
            temp1=temp1.next
            l+=1
        
        if pos <= l and pos > 0:
            while pos>1:
                temp2=temp
                temp=temp.next
                pos-=1
            temp2.next=temp.next
        else:
            print("Invalid position")
    
    #---------------------------------------------------------------------------------------------------

    #sort the linked list
    def sorting(self):
        
        temp = self.head
        temp2 = temp.next
        temp2 = self.head.next
        print("1.Ascending Order.\n2.Descending Order.")
        print("Please specify order")
        ch = int(input("Enter your choice\n"))
        if ch ==1:
            while temp.next:
                min = temp
                temp2 = temp.next
                while temp2:
                    if temp2.data < temp.data:
                        min = temp2
                        Node.swap_two(temp,min)
                    temp2 = temp2.next

                temp = temp.next
        else:
            while temp.next:
                min = temp
                temp2 = temp.next
                while temp2:
                    if temp2.data > temp.data:
                        min = temp2
                        Node.swap_two(temp,min)
                    temp2 = temp2.next

                temp = temp.next
        Insertion_Deletion.display_list(self)


    #----------------------------------------------------------------------------------------------------
    #search a Node
    def searching_pr(self,x):
        if self.head is None:
            return None
        
        else:
            temp = self.head

            while temp:
                if temp.data == x:
                    return True
                temp = temp.next
            return False

#-------------------------------------------------------------------------------------------------------
def main():
    linked_list = Insertion_Deletion()

    while True:
        print("\nOperations Menu:")
        print("1. Add Node")
        print("2. Insert at First")
        print("3. Insert at Last")
        print("4. Insert at Specific Position")
        print("5. Delete First")
        print("6. Delete Last")
        print("7. Delete at Specific Position")
        print("8. Sort Linked List")
        print("9. Search")
        print("10. Display Linked List")
        print("11. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data for the new node: "))
            linked_list.addNode_S(data)
        elif choice == 2:
            data = int(input("Enter data for the new node: "))
            linked_list.insert_first(data)
        elif choice == 3:
            data = int(input("Enter data for the new node: "))
            linked_list.insert_last(data)
        elif choice == 4:
            data = int(input("Enter data for the new node: "))
            pos = int(input("Enter the position: "))
            linked_list.insert_spec_pos(data, pos)
        elif choice == 5:
            linked_list.delete_first()
        elif choice == 6:
            linked_list.delete_last()
        elif choice == 7:
            pos = int(input("Enter the position: "))
            linked_list.delete_spec_pos(pos)
        elif choice == 8:
            linked_list.sorting()
        elif choice == 9:
            data = int(input("Enter data to search for: "))
            result = linked_list.searching_pr(data)
            if result:
                print("Data found in the list.")
            else:
                print("Data not found in the list.")
        elif choice == 10:
            linked_list.display_list()
        elif choice == 11:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        
#------------------------------------------------------------------------------------------       
#import all the .py file for use of operations
# if __name__ =='__main__':
#     s = Insertion_Deletion()
#     s.addNode_S(53)
#     s.addNode_S(23)

#     s.addNode_S(-923)
#     s.addNode_S(3)
#     s.insert_first(35)
#     s.display_list()
#     s.insert_last(-93)
#     s.display_list()
#     s.insert_spec_pos(34,4)
#     s.display_list()

#     s.sorting()
#     if s.searching_pr(23):
#         print("Element in")
#     else:
#         print("Element out")
    # s.delete_first()
    # s.display_list()

    # s.delete_last()
    # s.display_list()



    # s.delete_spec_pos(3)
    # s.display_list()




    

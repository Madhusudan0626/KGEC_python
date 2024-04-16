#Write a Python program that implements circular queue as a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.start = None

    def insert_cc_queue(self):
        item = int(input("Enter the value to be inserted: "))
        ptr = Node(item)

        if self.start is None:
            ptr.next = ptr
            self.start = ptr
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            ptr.next = temp.next
            temp.next = ptr

    def delete_cc_queue(self):
        if self.start is None:
            print("Underflow")
            return

        ptr = self.start
        if self.start.next == self.start:
            self.start = None
        else:
            temp = self.start
            while temp.next != self.start:
                temp = temp.next
            self.start = self.start.next
            temp.next = self.start

        print("Deleted element is:", ptr.data)
        del ptr

    def display(self):
        if self.start is None:
            print("Queue is empty.")
            return

        ptr = self.start
        while True:
            print("Data is", ptr.data)
            ptr = ptr.next
            if ptr == self.start:
                break

if __name__ == "__main__":
    cq = CircularQueue()

    while True:
        print("\n1.Insert in the circular queue.")
        print("2.Delete from the circular queue.")
        print("3.Display the queue.")
        print("4.Exit.")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            cq.insert_cc_queue()
        elif choice == 2:
            cq.delete_cc_queue()
        elif choice == 3:
            cq.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice.")

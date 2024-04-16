class IntNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


    @staticmethod
    def count42s(head):
        current = head
        while current is not None:
            if current.data != 42:
                return False
            current = current.next
        return True
    def print_list(head):
        current = head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print() 

head = IntNode(42, IntNode(42, IntNode(42, IntNode(42, IntNode(42, None)))))
print("The list")
IntNode.print_list(head)
print("Every node in list contain 42",IntNode.count42s(head))

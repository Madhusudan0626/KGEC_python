class IntNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    @staticmethod
    def count42s(head):
        current = head
        while current is not None:
            if current.data == 42:
                return True
            current = current.next
        return False

head = IntNode(1, IntNode(42, IntNode(3, IntNode(42, IntNode(5, None)))))
print("At least one occurrence of the number 42",IntNode.count42s(head))

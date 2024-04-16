class IntNode:
    def __init__(self, data=0, link=None):
        self.data = data
        self.link = link

    @staticmethod
    def count42s(head):
        count = 0
        current = head
        while current is not None:
            if current.data == 42:
                count += 1
            current = current.link
        return count

head = IntNode(1, IntNode(42, IntNode(3, IntNode(42, IntNode(5, None)))))
print("Number of 42s ",IntNode.count42s(head))

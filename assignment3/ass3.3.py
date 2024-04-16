class IntNode:
    def __init__(self, data=0, link=None):
        self.data = data
        self.link = link

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1,2):
        if n % i == 0:
            return False
    return True

def print_prime_numbers(head):
    current = head
    while current is not None:
        if is_prime(current.data):
            print(current.data)
        current = current.link

head = IntNode(11, IntNode(2, IntNode(3, IntNode(4, IntNode(5, None)))))
print_prime_numbers(head)

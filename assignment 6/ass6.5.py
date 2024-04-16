#Write a Python program that implements a priority queue using a linked list.

class Node:
    def __init__(self,val,priority):
        self.val = val
        self.priority = priority

    def __del__(self):
        print("Destructor")

    def __repr__(self) -> str:
        return "Node(val: {}, pri: {})".format(self.val,self.priority)
    

class PriorityQueue:
    def __init__(self):
        self.storage=[]

    def priorityCheck(self,p1,p2):
        return p1<p2
    
    def insert(self,val,priority):
        data = Node(val,priority)

        index_pro=0
        while index_pro < len(self.storage):
            if self.priorityCheck(self.storage[index_pro].priority,priority):
                break
            index_pro+=1

        self.storage.insert(index_pro,data)

    def peek(self):
        return self.storage[-1].val

    def pop(self):
        return self.storage.pop().val
    
    def display(self):
        print("Priority Queue")
        for item in self.storage:
            print("Value:",item.val," priority:",item.priority)
    

if __name__=="__main__":
    pq=PriorityQueue()
    pq.insert(78,3)
    pq.insert(873,1)
    pq.insert(781,2)
    print(pq.display())

    print("Remove item from queue",pq.pop())

    print("peek value",pq.peek())
    print(pq.display())
    



#stack
class stackpro:
    def __init__(self,size):
        self.size=size
        self.top = -1
        self.a = []*size
    def __del__(self):
        print("Destroy")
    def push_s(self,x):

        if self.top < self.size -1:
            self.top+=1
            self.a.append(x)
        else:
            print("Overflow")
        
    def pop_s(self):
        if self.top != -1:
            print("\nPoped Element",self.a[self.top])
            
            val = self.a[self.top]
            self.a=self.a[:self.top]
            self.top-=1
            return val
        print("\nUnderflow")
        
    def display(self):
        k=self.top
        print("\nThe stack-->")
        while k!=-1:
            print(self.a[k],end=" ")
            k-=1

def menu_stack():
    size = int(input("Enter the size of the stack: "))
    stack = stackpro(size)

    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter element to push: "))
            stack.push_s(element)
        elif choice == 2:
            stack.pop_s()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

# Main program
if __name__ == "__main__":
    menu_stack()
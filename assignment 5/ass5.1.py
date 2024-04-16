# Write a Python program to convert an infix expression into postfix expression
class Stack:
    def __init__(self,size):
        self.size=size
        self.top = -1
        self.a = []*size
    def __del__(self):
        print("Destruction")
    def push_s(self,x):

        if self.top < self.size -1:
            self.top+=1
            self.a.append(x)
        else:
            print("Overflow")
        
    def pop_s(self):
        if self.top != -1:
            
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


class Conversion:
    def __init__(self):
        pass

    def __del__(self):
        print("Destruction")
    def precedence(self,c):
        if c=='^':
            return 3
        elif c=='*' or c=='/' or c=='%':
            return 2
        elif c=='+' or c=='-':
            return 1
        else:
            return -1
    
    def isOperand(self,c):
        if '0'<=c<='9' or 'a'<=c<'z' or 'A'<=c<='Z':
            return True
        return False


    def associativity(self,c):
        if c == '^':
            return 'R'
        return 'L'

    def takeInfixex(self,s):
        st=Stack(len(s))
        result=""
        for i in s:
            if self.isOperand(i):
                result+=i
            elif i == '(':
                st.push_s(i)
            elif i==')':
                while st.a and st.a[st.top] != '(':
                    result+=str(st.pop_s())
                st.pop_s()
            else:
                while st.a and (self.precedence(i) < self.precedence(st.a[st.top]) 
                                or (self.precedence(i) == self.precedence(st.a[st.top]) 
                                    and self.associativity(i) == 'L')):
                    result+=st.pop_s()
                st.push_s(i)
        while st.a:
            result+=st.pop_s()
        print(result)


if __name__ =='__main__':
    
    c= Conversion()
    
    print("Equivalent postifix expression of 2+3-(5*5)")
    c.takeInfixex("(2+3)/(5*5)")

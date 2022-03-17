
class Stack:
    def __init__(self,maxsize) -> None:
        self.stack = []
        self.maxsize = maxsize
    
    def isEmpty(self):
        if len(self.stack):
            return True
        return False
    
    def isFull(self):
        if len(self.stack) == self.maxsize:
            return False
        return True
    
    def push(self,element):
        if self.isFull():
            self.stack.append(element)
        else:
            print('Stack is Full')
            
    def pop(self):
        if self.isEmpty():
            return self.stack.pop()
        else:
            print('Stack is Empty')
    def FindElement(self,element):
        if self.isEmpty():
            if element in self.stack:
                return f'Element Found at index : {self.stack.index(element)}'
            else:
                return 'Element Not Found'
        else:
            print('Stack is Empty')
            
    def data(self):
        if self.isEmpty():
            return self.stack
        else:
            print('Stack is Empty')
            
    def peek(self):
        if self.isEmpty():
            return self.stack[len(self.stack)-1]
        else:
            print('Stack is Empty')
            
            
st = Stack(5)
st.push(2)
st.data()
st.push(3)
st.peek()
st.pop()
st.FindElement(2)
            
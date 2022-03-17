class Queue:
    def __init__(self,maxlength) -> None:
        
        self.maxlength = maxlength
        self.queue = []*self.maxlength
        self.front = 0
        self.rear = 0
    # def isfull(self):
        
    def isEmpty(self):
        if self.front == self.rear:
            return False
        return True
    
    def inqueue(self,data):
        self.queue.insert(self.front,data)
        self.front +=1
        
    def dequeue(self):
        self.queue[self.rear] = None
        self.rear +=1
        
        
    
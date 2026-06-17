#circularqueue using array
class circularqueue:
    def __init__(self,size):
        self.queue=[None]*size
        self.size=size
        self.front=-1
        self.rear=-1
    def isEmpty(self):
        return self.front==-1
    def isFull(self):
        return (self.rear+1)%self.size==self.front
    def enqueue(self,data):
        if self.isFull():
            return "queue is full"
        if self.isEmpty():
            self.front=0
            self.rear=0
        else:
            self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=data
    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        data=self.queue[self.front]
        self.queue[self.front]=None
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return data
    def getfront(self):
        if self.isEmpty():
            return "queue empty"
        return self.queue[self.front]
    def getrear(self):
        if self.isEmpty():
            return "queue empty"
        return self.queue[self.rear]
    def traversal(self):
        if self.isEmpty():
            print("Queue Empty")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
cq=circularqueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.traversal()
cq.dequeue()
cq.traversal()
print(cq.getfront())
print(cq.getrear())
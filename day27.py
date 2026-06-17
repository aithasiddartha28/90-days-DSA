#Queues using array

class queue:
    def __init__(self,size):
        self.queue=[ None]*size
        self.size=size
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if self.rear==self.size-1:
            return "queue fail"
        if self.front==-1:
            self.front=0
        self.rear+=1
        self.queue[self.rear]=data
    def dequeue(self):
        if self.front==-1:
            return "queue empty"
        data=self.queue[self.front]
        self.queue[self.front]=None
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front+=1
        return data
    def getfront(self):
        return self.queue[self.front]
    def getrear(self):
        return self.queue[self.rear]
    def isempty(self):
        return self.front==self.rear==-1
    def isfull(self):
        return self.rear==self.size-1
    def traversal(self):
        print(self.queue)
q=queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(40)
q.traversal()
print(q.dequeue())
q.traversal()
print(q.getfront())
print(q.getrear())
print(q.isempty())
print(q.isfull())
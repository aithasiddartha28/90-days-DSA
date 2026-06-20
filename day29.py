#deque usng array
class deque:
    def __init__(self,size):
        self.deque=[None]*size
        self.size=size
        self.front=-1
        self.rear=-1
    def isEmpty(self):
        return self.front==-1 and self.rear==-1
    def isfull(self):
        return (self.rear+1)%self.size==self.front
    def insertrear(self,data):
        if self.isfull():
            return "deque is full"
        if self.isEmpty():
            self.front=0
            self.rear=0
        else:
            self.rear=(self.rear+1)%self.size
        self.deque[self.rear]=data
    def insertfront(self,data):
        if self.isfull():
            return "deque is full"
        if self.isEmpty():
            self.front=0
            self.rear=0
        else:
            self.front=(self.front-1+self.size)%self.size
        self.deque[self.front]=data
    def deletefront(self):
        if self.isEmpty():
            return "deque empty"
        temp=self.front
        self.deque[temp]=None
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.size
    def deleterear(self):
        if self.isEmpty():
            return "deque s empty"
        temp=self.rear
        self.deque[temp]=None
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.rear=(self.rear-1+self.size)%self.size
    def getfront(self):
        if self.isEmpty():
            return "dequeu empty"
        return self.deque[self.front]
    def getrear(self):
        if self.isEmpty():
            return "deque empty"
        return self.deque[self.rear]
    def traversal(self):
        print(self.deque)
d=deque(11)
d.insertrear(5)
d.insertrear(10)
d.insertrear(15)
d.insertrear(20)
d.insertrear(25)
d.insertfront(1)
d.insertfront(2)
d.insertfront(3)
d.insertfront(4)
print(d.deleterear())
print(d.deletefront())
print(d.getfront())
print(d.getrear())
d.traversal()
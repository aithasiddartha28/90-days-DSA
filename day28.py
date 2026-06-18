#Circular Queue using Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularQueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isempty(self):
        return self.front is None
    def enqueue(self,data):
        newNode=Node(data)
        if self.isempty():
            self.front=newNode
            self.rear=newNode
            self.rear.next=self.front
        else:
            newNode.next=self.front
            self.rear.next=newNode
            self.rear=newNode
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        data=self.front.data
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.rear.next=self.front
        return data
    def getfront(self):
        if self.isempty():
            return "queue is empty"
        return self.front.data
    def getrear(self):
        if self.isempty():
            return "queue is empty"
        return self.rear.data
    def traversal(self):
        if self.isempty():
            print("queue empty")
            return
        temp=self.front
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.front:
                break
        print("None")
cq=CircularQueue()
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
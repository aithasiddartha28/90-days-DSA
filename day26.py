class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        newNode=Node(data)
        if self.front is None:
            self.front=newNode
            self.rear=newNode
            return
        self.rear.next=newNode
        self.rear=newNode
    def dequeue(self):
        if self.front is None:
            return "queue empty"
        data=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear is None
        return data
    def getfront(self):
        if self.front is None:
            return "queue empty"
        return self.front.data
    def getrear(self):
        if self.rear is None:
            return "queue empty"
        return self.rear.data
    def isempty(self):
        return self.front is None
    def size(self):
        temp=self.front
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count
    def traversal(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.traversal()
q.dequeue()
q.traversal()
print("first element",q.getfront())
print("last element",q.getrear())
print(q.isempty())
print(q.size())
#Deque using Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
    def isempty(self):
        return self.front is None
    def insertfront(self,data):
        newNode=Node(data)
        if self.isempty():
            self.front=newNode
            self.rear=newNode
        else:
            newNode.next=self.front
            self.front=newNode
    def insertrear(self,data):
        newNode=Node(data)
        if  self.isempty():
            self.front=newNode
            self.rear=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
    def deletefront(self):
        if self.isempty():
            return "empty"
        data=self.front.next
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        return data
    def deleterear(self):
        if self.isempty():
            return "empty"
        data=self.rear.data
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            temp=self.front
            while temp.next!=self.rear:
                temp=temp.next
            temp.next=None
            self.rear=temp
        return data
    def traversal(self):
        temp=self.front
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
d=Deque()
d.insertfront(5)
d.insertfront(10)
d.insertfront(15)
d.insertfront(20)
d.insertrear(25)
d.insertrear(30)
d.insertrear(35)
d.insertrear(40)
d.traversal()
d.deletefront()
d.deleterear()
d.traversal()
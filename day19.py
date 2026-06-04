class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertbegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def insertend(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
    def traversal(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
    def backTraversal(self):
        temp=self.tail
        while temp:
            print(temp.data,end="->")
            temp=temp.prev
        print("None")
    def deletebegin(self,data):
        if self.head is None:
            return
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
    def deleteend(self,data):
        if self.head is None:
            return
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    def search(self,key):
        if self.head is None:
            return False
        temp=self.head
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        return False
    def deletevalue(self,data):
        if self.head is None:
            return
        temp=self.head
        while temp:
            if temp.data==data:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                return 
            temp=temp.next
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            newNode=curr.next
            curr.next=prev
            prev=curr
            curr=newNode
        self.head=prev
dll=DLL()
dll.insertbegin(10)
dll.insertbegin(20)
dll.insertbegin(30)
dll.insertbegin(5)
dll.insertend(100)
dll.deletebegin(5)
dll.deleteend(100)
dll.deletevalue(20)
dll.reverse()
print(dll.search(20))
dll.traversal()
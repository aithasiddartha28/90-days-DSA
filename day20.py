'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def traversal(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def insertbegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def insertEnd(self,data):
        newNode=Node(data)
        if self.tail is None:
            self.head=self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def searchvalue(self,data):
        if self.head is None:
            print("value not found")
        else:
            temp=self.head
            while temp:
                if temp.data==data:
                    print("found")
                temp=temp.next
    def deletebegin(self):
        if self.head is None:
            return
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
    def deleteend(self):
        if self.head is None:
            return 
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            temp.next=None
            self.tail=temp
    def reverse(self):
        if self.head is None:
            return
        else:
            prev=None
            curr=self.head
            while curr:
                newNode=curr.next
                curr.next=prev
                prev=curr
                curr=newNode
            self.head=prev 
sll=SLL()
sll.insertbegin(1)
sll.insertbegin(2)
sll.insertbegin(3)
sll.insertbegin(4)
sll.insertbegin(5)
sll.insertEnd(0)
sll.insertEnd(-1)
sll.insertEnd(-2)
sll.insertEnd(-3)
sll.searchvalue(2)
sll.deletebegin()
sll.deleteend()
sll.reverse()
sll.traversal()'''

















class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def traversal(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    def dllinsertbegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def dllinsertend(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
    def reverse(self):
        temp=self.tail
        while temp:
            print(temp.data,end="->")
            temp=temp.prev
        print("None")
    def dllsearch(self,data):
        if self.head is None:
            print("No data")
        else:
            temp=self.head
            while temp:
                if temp.data==data:
                    print("Found")
                temp=temp.next
    def dlldeletebegin(self):
        if self.head is None:
            return
        elif self.head==self.tail:
            self.tail=None
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None
    def dlldeleteend(self):
        if self.head is None:
            return 
        elif self.head==self.tail:
            self.tail=None
            self.head=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    def dlldeletevalue(self,data):
        if self.head is None:
            return
        temp=self.head
        while temp:
            if temp.data==data:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                return
            temp=temp.next
dll=DLL()
dll.dllinsertbegin(1)
dll.dllinsertbegin(2)
dll.dllinsertbegin(3)
dll.dllinsertbegin(4)
dll.dllinsertbegin(5)
dll.dllinsertend(0)
dll.dllinsertend(-1)
dll.dllinsertend(-2)
dll.dllinsertend(-3)
dll.dllinsertend(-4)
dll.dlldeletebegin()
dll.dlldeleteend()
dll.dlldeletevalue(2)
dll.traversal()
dll.reverse()
dll.dllsearch(0)
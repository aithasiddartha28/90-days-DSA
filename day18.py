class Node:
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
            print(temp.data,end='->')
            temp=temp.next
        print("None")
    def insertbegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            newNode=curr.next
            curr.next=prev
            prev=curr
            curr=newNode
        self.head=prev
sll=SLL()
sll.insertbegin(10)
sll.insertbegin(20)
sll.insertbegin(30)
sll.insertbegin(5)
sll.traversal()
sll.reverse()
sll.traversal()
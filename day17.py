#length of linkedlist
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
            print(temp.data)
            temp=temp.next
        print("None")
    def insertbegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def length(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count  
    def search(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        return False
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
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
        self.tail=temp
    def deletevalue(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            if self.head is None:
                self.tail=None
            return
        temp=self.head
        while temp.next and temp.next.data != data:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next

        if temp.next is None:
            self.tail = temp
        self.temp=self.head
        if self.temp.data==data:
            temp=temp.next
    
sll=SLL()
sll.insertbegin(10)
sll.insertbegin(20)
sll.insertbegin(30)
sll.insertbegin(5)
sll.traversal()
sll.deletebegin()
sll.deleteend()
sll.deletevalue(20)
sll.traversal()
'''print(sll.length())
print(sll.search(20))'''
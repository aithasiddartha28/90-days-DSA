class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
    def pop(self):
        if self.top is None:
            print("stack empty")
        data=self.top.data
        self.top=self.top.next
        return data
    def peek(self):
        if self.top is None:
            return "Stack empty"
        return self.top.data
    def isempty(self):
        return self.top is None
    def traversal(self):
        temp=self.top
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
S=Stack()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
S.traversal()
S.pop()
print(S.peek())
print(S.isempty())

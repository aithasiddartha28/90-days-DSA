'''#stacks using Arrys
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack)==0:
            return "stack empty"
        return self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return "empty stack"
        return self.stack[-1]
    def isempty(self):
        if len(self.stack)==0:
            return True
        return False
    def display(self):
        print(self.stack)
S=Stack()
S.push(10)
S.push(20)
S.push(30)
print(S.display())
S.pop()
print(S.isempty())
print(S.peek())
print(S.stack)'''

#stacks using Linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
    def pop(self):
        if self.top is None:
            return "stack empty"
        data=self.top.data
        self.top=self.top.next
        return data
    def peek(self):
        if self.top is None:
            return "stack empty"
        return self.top.data
    def isempty(self):
        return self.top is None
    def travers(self):
        temp=self.top
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("poped",s.pop())
print("peek",s.peek())
print(s.isempty())
s.travers()
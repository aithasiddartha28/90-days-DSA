#insert at beginning
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
first=Node(10)
secound=Node(20)
third=Node(30)
first.next=secound
secound.next=third
new=Node(5)
new.next=first
first=new
current=first
while current:
    print(current.data)
    current=current.next'''
    
#insert at end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
first=Node(10)
secound=Node(20)
third=Node(30)
new=Node(40)
first.next=secound
secound.next=third
third.next=new
current=first
count=0
while current:
    print(current.data)
    count+=1
    current=current.next
print(count)
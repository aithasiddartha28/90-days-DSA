class Minheap:
    def __init__(self):
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self.heapifyup()
    def delete(self):
        if len(self.heap)==0:
            return "heap is empty"
        if len(self.heap)==1:
            return self.heap.opp()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapifydown()
        return root
    def heapifyup(self):
        i=len(self.heap)-1
        while i>0:
            parent=(i-1)//2
            if self.heap[i]<self.heap[parent]:
                self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
                i=parent
            else:
                break
    def heapifydown(self):
        i=0
        while True:
            left=2*i+1
            right=2*i+2
            smallest=i
            
            if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
                smallest=left
            if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
                smallest=right
            if smallest==i:
                break
            self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
            i=smallest
        
m=Minheap()
m.insert(50)
m.insert(40)
m.insert(30)
m.insert(20)
m.insert(10)
m.delete()
print(m.heap)
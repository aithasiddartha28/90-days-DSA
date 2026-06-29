class Maxheap:
    def __init__(self):
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self.heapifyup()
    def delete(self):
        if len(self.heap)==0:
            return "heap empty"
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapipdown()
        return root
    def heapifyup(self):
        i=len(self.heap)-1
        while i>0:
            parent=(i-1)//2
            if self.heap[i]>self.heap[parent]:
                self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
                i=parent
            else:
                break
    def heapipdown(self):
        i=0
        while True:
            left=2*i+1
            right=2*i+2
            highest=i
            if left<len(self.heap) and self.heap[left]>self.heap[highest]:
                highest=left
            if right<len(self.heap) and self.heap[right]>self.heap[highest]:
                highest=right
            if highest==i:
                break
            self.heap[i],self.heap[highest]=self.heap[highest],self.heap[i]
            i=highest
max=Maxheap()
max.insert(10)
max.insert(20)
max.insert(30)
max.insert(40)
max.insert(50)
print(max.heap)
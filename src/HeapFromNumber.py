class Heap:
    def __init__(self):
        self.heap=[]
   
    def _index_left(self,i):
        return 2*i+1
    def _index_parent(self,i):
        return (i-1)//2
    def _index_right(self,i):
        return 2*i+2
    def _heapifyUp(self,i):
        if i>0 and self.heap[i]>self.heap[self._index_parent(i)]:
           temp= self.heap[i]
           self.heap[i]=self.heap[self._index_parent(i)]
           self.heap[self._index_parent(i)]=temp
           self.heap=self._heapifyUp(self._index_parent(i))
        return  self.heap   
    def push(self,value):
        self.heap.append(value)
        self.heap=self._heapifyUp(len(self.heap)-1)
    def display(self):
        for vr in self.heap:
            print(vr, end =" ")    


def main():
    hp=Heap()
    hp.push(1)
    hp.push(5)
    hp.push(2)
    hp.push(3)
    hp.push(10)
    hp.display()

if __name__=="__main__":
    main()
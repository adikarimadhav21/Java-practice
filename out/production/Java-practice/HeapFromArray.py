class Heap:
    def __init__(self):
        self.heap=[]
    def _index_left(self,i):
        return 2*i+1 
    def _index_right(self,i):
        return 2*i+2
    def _index_parent(self,i) :
        return (i-1)//2  
    def _heapifyDown(self,i,size):
        largest=i
        left=self._index_left(i)
        right=self._index_right(i)
        if left<size and self.heap[i]<self.heap[left]:
            largest=left
        if right<size and self.heap[right]>self.heap[largest]:
            largest= right
        if i!=largest:
            temp=self.heap[i]
            self.heap[i] =self.heap[largest]
            self.heap[largest]=temp
            self._heapifyDown(largest,size)
    def heapifyDown(self,input):
        size=len(input)
        self.heap=input
        for i in range((size//2-1),-1,-1): # end should be zero 0 but range -1 not inlcude so 0
            self._heapifyDown(i,size)

    def display(self):
        for a in self.heap:
            print(a,end=' ') 

def main():
    input=[1,5,2,3,10]
    hp=Heap()
    hp.heapifyDown(input)
    hp.display()

if __name__=="__main__":
    main()




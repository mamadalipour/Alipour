class minheap:
    def __init__ (self):
        self.heap=[]

    def insert (self,value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) -1)

    def _heapify_up(self,index):
        parent_index = (index-1)//2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index] , self.heap[parent_index] = self.heap[parent_index],self.heap[index]
            self._heapify_up(parent_index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_value = self.heap[0]
        last_value= self.heap.pop()
        if len (self.heap)>0:
            self.heap[0]= last_value 
            self._heapify_down(0)
        return min_value
    
    def _heapify_down(self , index):
        left_child_index= 2*index+1
        right_child_index=2*index+2
        smallest= index
        if (left_child_index<len(self.heap)and self.heap[left_child_index]<self.heap[smallest]):
            smallest=left_child_index
        if(right_child_index<len(self.heap)and self.heap[right_child_index]<self.heap[smallest]):
            smallest=right_child_index
        if smallest != index:
            self.heap[index],self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def heapsort(arry):
        heap = minheap()
        for item in arry :
            heap.insert(item)
        sorted_arry=[]
        for _ in range(len(arry)):
            sorted_arry.append(heap.extract_min())
        return sorted_arry
    
input_data= [20 , 8 , 5, 1 , 12, 25]
sorted_output = heapsort(input_data)
print(sorted_output)


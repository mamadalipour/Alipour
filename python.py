class queue:
    def __init__(self , max_size):
        self.max_size = max_size
        self.Q=[0]* max_size
        self.num=0
        self.num=0
        self.first=0
    def enqueue(self,item):
        if self.num>= self.max_size:
            raise Exception("queue overflow")
        self.Q[(self.num + self.first)% self.max_size]= item 
        self.num+=1
    def dequeue(self):
        if self.num==0:
            raise Exception("queue empty")
        item= self.Q[self.first] 
        self.first=(self.first+1)% self.max_size
        self.num -=1
        return item
    def front(self):
        if self.num==0:
            raise Exception("queue empty")
        return self.Q[self.first]
    

    def is_empty(self):
        return self.num==0
    
    def size(self) :
        return self.num
    
    def is_full(self):
        return self.num >= self.max_size
    
    def get_element(queue, num):
        if i < len(queue):
            return queue[num]
        else:
            return None


q=queue(10)
q.enqueue("rana")
q.enqueue("vez")
q.enqueue("arya")
print("queue size is :",q.size())
print(q.dequeue(), "left queue")
print("front of queue is:",q.front())
q.enqueue("milad")
q.dequeue()
q.dequeue()
q.enqueue("ali")

print ("get i =" ,q.get_element())
print("it was a queue")








    
     
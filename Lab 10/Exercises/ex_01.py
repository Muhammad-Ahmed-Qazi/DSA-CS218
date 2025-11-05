class Queue:
    def __init__(self, maxLength = 10):
        self.maxLength = maxLength
        self.items = [None for i in range(maxLength)]
        self.make_null()

    def add_one(self, i):
        return ((i+ 1) % self.maxLength)
    
    def make_null(self):
        self.front = 0
        self.rear = self.maxLength - 1
    
    def empty(self):
        if self.add_one(self.rear) == self.front:
            return True
        return False
    
    def toq(self):
        if self.empty():
            print("Queue is Empty!")
        else:
            return self.items[self.front]
    
    def enqueue(self, value):
        if self.add_one(self.add_one(self.rear)) == self.front:
            print("Queue is Full!")
        else: 
            self.rear = self.add_one(self.rear)
            self.items[self.rear] = value
    
    def dequeue(self):
        if self.empty():
            print("Queue is Empty!")
        else:
            value = self.items[self.front]
            self.items[self.front] = None  # optional, good for debugging
            self.front = self.add_one(self.front)
            return value


# Main program
if __name__ == '__main__':
    myQueue = Queue(5)
    print("Is the queue empty?", myQueue.empty())  # Expected: True
    myQueue.enqueue(10)
    myQueue.enqueue(20)
    print("Is the queue empty after enqueuing?", myQueue.empty())  # Expected: False
    print("Front item:", myQueue.toq())  # Expected: 10
    print("Dequeued item:", myQueue.dequeue())  # Expected: 10
    print("Front item after dequeue:", myQueue.toq())  # Expected: 20
    print("Dequeued item:", myQueue.dequeue())  # Expected: 20
    print("Is the queue empty after dequeuing all items?", myQueue.empty())  #


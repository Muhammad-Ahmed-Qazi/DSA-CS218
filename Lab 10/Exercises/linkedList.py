# Implement EMPTY, ENQUEUE, DEQUEUE algorithms using a Linked List

class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def getItem(self):
        return self.item
    
    def getNext(self):
        return self.next
    
    def setItem(self, item):
        self.item = item

    def setNext(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None)  # Sentinel node
        self.tail = self.head
        self.size = 0
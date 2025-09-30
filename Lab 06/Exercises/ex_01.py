from node import Node

class LinkedList:
    def __init__(self):
        self.head = Node(None)  # Sentinel node
        self.tail = self.head
        self.size = 0
    
# Created a linked list object
linked_list = LinkedList()
from linkedList import Node,LinkedList

# A 10.3 -- Empty
def is_empty(linked_list):
    return linked_list.size == 0

# A 10.5 -- Enqueue
def enqueue(linked_list, item):
    new_node = Node(item)
    linked_list.tail.setNext(new_node)
    linked_list.tail = new_node
    linked_list.size += 1

# A 10.6 -- Dequeue
def dequeue(linked_list):
    if is_empty(linked_list):
        return None
    item = linked_list.head.getNext().getItem()
    linked_list.head = linked_list.head.getNext()
    linked_list.size -= 1
    return item

# Main program
# Created a linked list object
linked_list = LinkedList()

# Testing EMPTY
print("Is the linked list empty?", is_empty(linked_list))  # Expected: True
# Testing ENQUEUE
enqueue(linked_list, 10)
enqueue(linked_list, 20)
print("Is the linked list empty after enqueuing?", is_empty(linked_list))  # Expected: False
# Testing DEQUEUE
print("Dequeued item:", dequeue(linked_list))  # Expected: 10
print("Dequeued item:", dequeue(linked_list))  # Expected: 20

print("Is the linked list empty after dequeuing all items?", is_empty(linked_list))  # Expected: True
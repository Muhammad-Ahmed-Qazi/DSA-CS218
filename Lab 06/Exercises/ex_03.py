"""A doubly linked list is one in which there are two pointers (next variables) in a node, one pointing
to the next node and the other pointing to the previous node. Design all above algorithms for a
doubly linked list and use them in a program."""

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None      # Pointer to next node
        self.prev = None      # Pointer to previous node
    
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)  # Sentinel node for easier edge case handling
        self.tail = self.head   # Initially, tail is the same as head
        self.size = 0           # Tracks number of elements

# Inserting a new node according to index position
def insert_at_index(dll, index, value):
    position = 0
    current = dll.head

    # Only insert if index is within bounds
    if index <= (dll.size):
        # Traverse to the node just before the desired index
        while position < index:
            current = current.next
            position += 1
        new_node = Node(value)
        # Insert new_node after 'current'
        new_node.next = current.next
        new_node.prev = current
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
        # Update tail if inserted at the end
        if new_node.next is None:
            dll.tail = new_node
        dll.size += 1
    else:
        print("Index out of bounds!")
    
    return dll

# Searching for an item
def search(dll, value):
    current = dll.head.next  # Skip sentinel node
    position = 0

    # Traverse the list to find the value
    while current is not None:
        if current.item == value:
            return position
        current = current.next
        position += 1

    return None  # Value not found

# Deleting the node on the basis of match
def delete_by_value(dll, value):
    # Special case: only one element in the list
    if dll.size == 1:
        dll.head.next = None
        dll.tail = dll.head
        dll.size -= 1
    else:
        current = dll.head.next
        # Traverse to find the node with the value
        while current is not None:
            if current.item == value:
                # Update pointers to remove current node
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                # Update tail if needed
                if current == dll.tail:
                    dll.tail = current.prev
                dll.size -= 1
                return dll
            current = current.next
        print("Value not found!")
    
    return dll

def display_list(dll):
    current = dll.head.next  # Skip sentinel node
    items = []
    # Collect all items in the list
    while current is not None:
        items.append(current.item)
        current = current.next
    print("Doubly Linked List:", " <-> ".join(map(str, items)))

# Main program
# Created a doubly linked list object
dll = DoublyLinkedList()

# Insert elements at specified indices
dll = insert_at_index(dll, 0, 10)
dll = insert_at_index(dll, 1, 20)
dll = insert_at_index(dll, 1, 15)  # Insert 15 at index 1

display_list(dll)  # Print the list

print("Position of 15:", search(dll, 15))  # Search for 15

dll = delete_by_value(dll, 15)  # Delete node with value 15
display_list(dll)               # Print the list after deletion

print("Position of 15 after deletion:", search(dll, 15))  # Search for 15 again
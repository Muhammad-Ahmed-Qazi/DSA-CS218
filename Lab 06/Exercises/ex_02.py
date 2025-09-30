from ex_01 import LinkedList
from node import Node

# Inserting a new node according to index position
def insert_at_index(linked_list, index, value):
    position = 0
    current = linked_list.head

    if index <= (linked_list.size):
        while position < index:
            current = current.next
            position += 1
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        linked_list.size += 1
    else:
        print("Index out of bounds!")
    
    return linked_list

# Searching for an item
def search(linked_list, value):
    current = linked_list.head.next  # Skip sentinel node
    position = 0

    while current is not None:
        if current.item == value:
            return position
        current = current.next
        position += 1

    return None  # Value not found

# Deleting the node on the basis of match
def delete_by_value(linked_list, value):
    if linked_list.size == 1:
        linked_list.head.next = None
    else:
        previous = linked_list.head
        current = linked_list.head.next
        while current is not None:
            if current.item == value:
                previous.next = current.next
                linked_list.size -= 1
                return linked_list
            previous = current
            current = current.next
        print("Value not found!")
    
    return linked_list

def display_list(linked_list):
    current = linked_list.head.next  # Skip sentinel node
    items = []
    while current is not None:
        items.append(current.item)
        current = current.next
    print("Linked List:", " -> ".join(map(str, items)))

# Main program
# Created a linked list object
linked_list = LinkedList()

linked_list = insert_at_index(linked_list, 0, 10)
linked_list = insert_at_index(linked_list, 1, 20)
linked_list = insert_at_index(linked_list, 1, 15)

display_list(linked_list)  # Output: Linked List: 10 -> 15 -> 20

print("Index of 15:", search(linked_list, 15))  # Output: Index of 15: 1
print("Index of 25:", search(linked_list, 25))  # Output: Index of 25: None

linked_list = delete_by_value(linked_list, 15)
print("Index of 15 after deletion:", search(linked_list, 15))  # Output: Index of 15 after deletion: None

linked_list = delete_by_value(linked_list, 30)  # Output: Value not found!

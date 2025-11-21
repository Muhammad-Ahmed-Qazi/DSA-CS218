def HeapInsertion(array, value):
    array.append(value)
    index = len(array) - 1
    while index > 0:
        parent_index = (index - 1) // 2
        if array[parent_index] < array[index]:
            array[parent_index], array[index] = array[index], array[parent_index]
            index = parent_index
        else:
            break
    return array

def HeapDelete(array):
    if len(array) == 0:
        return None, array   # or raise error
    
    root_value = array[0]
    last_value = array.pop()

    # Case: only 1 element was in the heap
    if len(array) == 0:
        return root_value, array   # return tuple!

    array[0] = last_value
    index = 0

    while True:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest_index = index

        if left_child_index < len(array) and array[left_child_index] > array[largest_index]:
            largest_index = left_child_index
        if right_child_index < len(array) and array[right_child_index] > array[largest_index]:
            largest_index = right_child_index

        if largest_index != index:
            array[index], array[largest_index] = array[largest_index], array[index]
            index = largest_index
        else:
            break

    return root_value, array


def HeapSort(array):
    sorted_array = []
    while len(array) > 0:
        max_value, array = HeapDelete(array)
        sorted_array.insert(0, max_value)
    return sorted_array

# Main program
if __name__ == "__main__":
    heap = []
    values_to_insert = [5, 3, 8, 1, 2, 7]

    for value in values_to_insert:
        heap = HeapInsertion(heap, value)
        print(f"Heap after inserting {value}: {heap}")

    print("\nDeleting elements from heap:")
    while len(heap) > 0:
        max_value, heap = HeapDelete(heap)
        print(f"Deleted {max_value}, new heap: {heap}")

    # Rebuild the heap for sorting
    for value in values_to_insert:
        heap = HeapInsertion(heap, value)

    sorted_array = HeapSort(heap)
    print(f"\nSorted array: {sorted_array}")
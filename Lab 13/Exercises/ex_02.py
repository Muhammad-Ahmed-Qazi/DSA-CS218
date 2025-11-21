def HeapInsertion(array, value):
    array.append(value)
    index = len(array) - 1

    # Bubble up (parent must be smaller for min-heap)
    while index > 0:
        parent_index = (index - 1) // 2
        if array[parent_index] > array[index]:
            array[parent_index], array[index] = array[index], array[parent_index]
            index = parent_index
        else:
            break
    return array


def HeapDelete(array):
    if len(array) == 0:
        return None, array

    root_value = array[0]
    last_value = array.pop()

    if len(array) == 0:
        return root_value, array

    array[0] = last_value
    index = 0

    # Bubble down (children must be larger for min-heap)
    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(array) and array[left] < array[smallest]:
            smallest = left
        if right < len(array) and array[right] < array[smallest]:
            smallest = right

        if smallest != index:
            array[index], array[smallest] = array[smallest], array[index]
            index = smallest
        else:
            break

    return root_value, array


def HeapSort(array):
    sorted_array = []
    while len(array) > 0:
        min_value, array = HeapDelete(array)
        sorted_array.append(min_value)     # already sorted in ascending order

    return sorted_array


# Main program
heap = [8, 22, 33, 25, 44, 40, 55, 55, 33]

heap = HeapInsertion(heap, 11)
print(f"Heap after inserting 11: {heap}")
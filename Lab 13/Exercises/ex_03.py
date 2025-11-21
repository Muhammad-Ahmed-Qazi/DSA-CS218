from ex_01 import HeapInsertion, HeapDelete, HeapSort

heap_a = []
heap_b = []
values_to_insert_a = [44, 33, 11, 55, 77, 90, 40, 60, 99, 22, 88, 66]
values_to_insert_b = ['D', 'A', 'T', 'A', 'S', 'T', 'R', 'U', 'C', 'T', 'U', 'R', 'E', 'S']

for value in values_to_insert_a:
    heap_a = HeapInsertion(heap_a, value)

for value in values_to_insert_b:
    heap_b = HeapInsertion(heap_b, value)

print(f"Sorted array (a): {HeapSort(heap_a)}")
print(f"Sorted array (b): {HeapSort(heap_b)}")
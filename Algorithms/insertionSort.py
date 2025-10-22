def insertionSort(arr):
    # print("Initial array:", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # print(f"\nInserting {key} at position {i}")
        while j >= 0 and arr[j] > key:
            # print(f"  {arr[j]} > {key}, shifting {arr[j]} to position {j+1}")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # print(f"Inserted {key} at position {j+1}, current array: {arr}")
    # print("\nSorted array:", arr)
    return arr

arr = [7, 4, 1, 2, 3, 9, 100, -10]
print(insertionSort(arr))
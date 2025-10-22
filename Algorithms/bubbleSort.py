def bubbleSort(arr):
    # c = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # print(i, j, arr[j], arr[j + 1])
                # c += 1
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    # return arr, c
    return arr

arr = [7, 4, 1, 2, 3, 9, 100, -10]
print(bubbleSort(arr))
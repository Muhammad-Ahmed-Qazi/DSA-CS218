def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp
    
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr

# Main program
arr = [7, 4, 1, 2, 3, 9, 100, -10]
print("Insertion Sort:", insertion_sort(arr))
print("Shell Sort:", shell_sort(arr))
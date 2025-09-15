import timeit

def binSearch_display(data, item):
    beg = 0
    end = len(data) - 1
    mid = int((beg + end) / 2)
    print("Beg:", beg, " End:", end, " Mid:", mid)

    while (beg <= end) and data[mid] != item:
        if item < data[mid]:
            end = mid - 1
            print("Beg:", beg, " \033[1mEnd:", end, "\033[0m Mid:", mid)
        else:
            beg = mid + 1
            print("\033[1mBeg:", beg, "\033[0m End:", end, " Mid:", mid)

        mid = int((beg + end) / 2)
    
    if data[mid] == item:
        return mid
    else:
        return None

def binSearch(data, item):
    beg = 0
    end = len(data) - 1
    mid = int((beg + end) / 2)

    while (beg <= end) and data[mid] != item:
        if item < data[mid]:
            end = mid - 1
        else:
            beg = mid + 1

        mid = int((beg + end) / 2)
    
    if data[mid] == item:
        return mid
    else:
        return None

# Main program
# data = [1, 2, 3, 4, 5]
# data = list(range(1, 10001))  # Example sorted list
data = []
userInp = 0
print("Choose the data type of data items to be inserted: \n1. Integer\n2. Float\n3. String")
data_type = int(input("Enter your choice (1/2/3): "))
if data_type not in [1, 2, 3]:
    print("Invalid choice! Defaulting to Integer.")
    data_type = 1

print("ALERT! Please enter sorted data!\nBegin entering data items one by one. Enter 'EXIT' to exit.")
while True:
    userInp = input(">>> ")
    if userInp != 'EXIT':
        if data_type == 1:
            userInp = int(userInp)
        elif data_type == 2:
            userInp = float(userInp)
        # For strings, no conversion needed
        data.append(userInp)
    else:
        print("Exiting data input.\n")
        break

item = input("Enter the item to search for: ")
if data_type == 1:
    item = int(item)
elif data_type == 2:
    item = float(item)

result = binSearch_display(data, item)
if result is not None:
    print("\nItem found at index:", result, end="\n")
else:
    print("\nItem not found!\n")

# Timing the function
execution_time = timeit.timeit('binSearch(data, item)', globals=globals(), number=1)
print(f"Execution time over 1 run: {execution_time} seconds")

# Built-in search method
def built_in_search(data, item):
    try:
        return data.index(item)
    except ValueError:
        return None
    
builtin_time = timeit.timeit('built_in_search(data, item)', globals=globals(), number=1)
print(f"Built-in search execution time over 1 run: {builtin_time} seconds")

# Comparing execution times
print("The custom search method is so much times slower than the built-in method:", execution_time / builtin_time)
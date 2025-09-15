import timeit

def custom_insert(array, pos, data):
    list_1 = array[:pos]
    list_2 = array[pos:]
    list_1 += [data]

    return list_1 + list_2

def binSearch(data, item, order_type):
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
        return (1, mid)
    else:
        if order_type == 1:  # Ascending
            return (0, custom_insert(data, beg, item))
        else:  # Descending
            print("Descending")
            return (0, custom_insert(data, end - 1, item))

def checkOrderAsc(prev, curr):
    return prev <= curr
def checkOrderDesc(prev, curr):
    return prev >= curr

# Main program
# data = [1, 2, 3, 4, 5]
# data = list(range(1, 10001))  # Example sorted list
data = []
userInp = 0
prev = None

print("Choose the data type of data items to be inserted: \n1. Integer\n2. Float\n3. String")
data_type = int(input("Enter your choice (1/2/3): "))
if data_type not in [1, 2, 3]:
    print("Invalid choice! Defaulting to Integer.")
    data_type = 1

print("Choose the order of sorting: \n1. Ascending\n2. Descending")
order_type = int(input("Enter your choice (1/2): "))
if order_type not in [1, 2]:
    print("Invalid choice! Defaulting to Ascending.")
    order_type = 1

checkOrder = checkOrderAsc if order_type == 1 else checkOrderDesc

print("ALERT! Please enter sorted data!\nBegin entering data items one by one. Enter 'EXIT' to exit.")
while True:
    userInp = input(">>> ")
    if userInp != 'EXIT':
        if data_type == 1:
            userInp = int(userInp)
        elif data_type == 2:
            userInp = float(userInp)
        # For strings, no conversion needed
        
        if prev is not None and not checkOrder(prev, userInp):
            print("Data not in sorted order! Please enter a valid item.")
            continue
        data.append(userInp)
        prev = userInp
    else:
        print("Exiting data input.\n")
        break

item = input("Enter the item to search for: ")
if data_type == 1:
    item = int(item)
elif data_type == 2:
    item = float(item)

result = binSearch(data, item, order_type)
if result[0] == 1:
    print("\nItem found at index:", result[1], end="\n")
else:
    print("\nItem not found! List updated!")
    print("Updated list:", result[1], end="\n")

# Timing the function
execution_time = timeit.timeit('binSearch(data, item, order_type)', globals=globals(), number=1)
print(f"Execution time over 1 run: {execution_time} seconds")

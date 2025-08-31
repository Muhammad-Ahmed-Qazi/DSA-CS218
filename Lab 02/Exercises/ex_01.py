# Insertion, Deletion, Searching - List
import timeit

lst = [23, 43, (5, 6), [], "Three"]
lst2 = [23, 43, (5, 6), [], "Three"]

def custom_insert(data, pos):
    global lst
    
    list_1 = lst[:pos]
    list_2 = lst[pos:]
    list_1 += [data]

    lst = list_1 + list_2

def custom_delete(data):
    global lst
    
    for i in range(len(lst)):
        if lst[i] == data:
            print(lst[i], data)
            list_1 = lst[:i]
            list_2 = lst[(i + 1):]
            lst = list_1 + list_2
            return
    print("Data not found!")

def custom_search(data):
    global lst

    for i in range(len(lst)):
        if lst[i] == data:
            return i
        else:
            return -1

# Main program
# Testing insertion
print("Insertion on first position:")
print("Original list1:", lst)
exec_time_custom_insert = timeit.timeit(lambda: custom_insert(45, 0), number=1)
print("Final list1:", lst)
print("Original list2:", lst2)
exec_time_builtin_insert = timeit.timeit(lambda: lst2.insert(0, 45), number=1)
print("Final list2:", lst2)
print("\nTime for custom insert:", exec_time_custom_insert)
print("Time for built-in insert:", exec_time_builtin_insert)
print("My function is so much slower than the built-in function:", exec_time_custom_insert / exec_time_builtin_insert)

# Testing deletion
print("\nDeletion:")
print("Original list1:", lst)
exec_time_custom_delete = timeit.timeit(lambda: custom_delete(43), number=1)
print("Final list1:", lst)
print("Original list2:", lst2)
exec_time_builtin_delete = timeit.timeit(lambda: lst2.remove(43), number=1)
print("Final list2:", lst2)
print("\nTime for custom delete:", exec_time_custom_delete)
print("Time for built-in delete:", exec_time_builtin_delete)
print("My function is so much slower than the built-in function:", exec_time_custom_delete / exec_time_builtin_delete)

# Testing searching
print("\nSearching:")
print("Original list1:", lst)
exec_time_custom_search = timeit.timeit(lambda: custom_search(23), number=1)
print("Original list2:", lst2)
exec_time_builtin_search = timeit.timeit(lambda: lst2.index(23), number=1)
print("\nTime for custom search:", exec_time_custom_search)
print("Time for built-in search:", exec_time_builtin_search)
print("My function is so much slower than the built-in function:", exec_time_custom_search / exec_time_builtin_search)
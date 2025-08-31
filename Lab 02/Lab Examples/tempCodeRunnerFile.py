# Insertion, Deletion, Searching - List
import timeit

lst = [23, 43, (5, 6), [], "Three"]

def custom_insert(data, pos, lst_p):
    
    list_1 = lst_p[:pos + 1]
    list_2 = lst_p[(pos + 1):]
    list_1 += [data]
    
    print("Final list:", list_1 + list_2)

def custom_delete(data, lst_p):
    for i in range(len(lst_p)):
        if lst_p[i] == data:
            print(lst_p[i], data)
            list_1 = lst_p[:i]
            list_2 = lst_p[(i + 1):]
            print("Final list:", list_1 + list_2)
            return
    print("Data not found!")

def custom_search(data, lst_p):
    for i in range(len(lst_p)):
        if lst_p[i] == data:
            return i
        else:
            return -1

# Main program
# Testing insertion
print("Insertion:")
print("Original list:", lst)
exec_time_custom_insert = timeit.timeit(lambda: custom_insert(45, 0, lst), number=1)
exec_time_builtin_insert = timeit.timeit(lambda: lst.insert(0, 45), number=1)
print("\nTime for custom insert:", exec_time_custom_insert)
print("Time for built-in insert:", exec_time_builtin_insert)
print("My function is so much slower/faster than the built-in:", exec_time_custom_insert / exec_time_builtin_insert)

# Testing deletion
print("\nDeletion:")
print("Original list:", lst)
exec_time_custom_delete = timeit.timeit(lambda: custom_delete(43, lst), number=1)
exec_time_builtin_delete = timeit.timeit(lambda: lst.remove(43), number=1)
print("\nTime for custom delete:", exec_time_custom_delete)
print("Time for built-in delete:", exec_time_builtin_delete)
print("My function is so much slower/faster than the built-in:", exec_time_custom_delete / exec_time_builtin_delete)

# Testing searching
print("\nSearching:")
print("Original list:", lst)
exec_time_custom_search = timeit.timeit(lambda: custom_search(23, lst), number=1)
exec_time_builtin_search = timeit.timeit(lambda: lst.index(23), number=1)
print("\nTime for custom search:", exec_time_custom_search)
print("Time for built-in search:", exec_time_builtin_search)
print("My function is so much slower/faster than the built-in:", exec_time_custom_search / exec_time_builtin_search)
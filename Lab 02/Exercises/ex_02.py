# Insertion, Deletion, Searching - Dictionary
import timeit

dct = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
dct2 = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

def custom_insert(key, value):
    global dct

    dict_1 = dct.copy()
    dict_2 = {key: value}

    dct = dict_1 | dict_2

def custom_delete(key):
    global dct

    for k in dct:
        if k in dct:
            dict_1 = dct.copy()
            del dict_1[k]
            dct = dict_1
            return
    print("Key not found!")

def custom_search(key):
    global dct

    for k in dct:
        if k == key:
            return dct[k]
    return -1

# Main program
# Testing insertion
print("Insertion of new key-value pair:")
print("Original dict1:", dct)
exec_time_custom_insert = timeit.timeit(lambda: custom_insert(6, "Six"), number=1)
print("Final dict1:", dct)
print("Original dict2:", dct2)
exec_time_builtin_insert = timeit.timeit(lambda: dct2.__setitem__(6, "Six"), number=1)
print("Final dict2:", dct2)
print("\nTime for custom insert:", exec_time_custom_insert)
print("Time for built-in insert:", exec_time_builtin_insert)
print("My function is so much slower than the built-in function:", exec_time_custom_insert / exec_time_builtin_insert)

# Testing deletion
print("\nDeletion of a key:")
print("Original dict1:", dct)
exec_time_custom_delete = timeit.timeit(lambda: custom_delete(3), number=1)
print("Final dict1:", dct)
print("Original dict2:", dct2)
exec_time_builtin_delete = timeit.timeit(lambda: dct2.pop(3, None), number=1)
print("Final dict2:", dct2)
print("\nTime for custom delete:", exec_time_custom_delete)
print("Time for built-in delete:", exec_time_builtin_delete)
print("My function is so much slower than the built-in function:", exec_time_custom_delete / exec_time_builtin_delete)

# Testing searching
print("\nSearching for a key:")
print("Dict1:", dct)
exec_time_custom_search = timeit.timeit(lambda: custom_search(4), number=1)
print("Result from custom search:", custom_search(4))
print("Dict2:", dct2)
exec_time_builtin_search = timeit.timeit(lambda: dct2.get(4, -1), number=1)
print("Result from built-in search:", dct2.get(4, -1))
print("\nTime for custom search:", exec_time_custom_search)
print("Time for built-in search:", exec_time_builtin_search)
print("My function is so much slower than the built-in function:", exec_time_custom_search / exec_time_builtin_search)


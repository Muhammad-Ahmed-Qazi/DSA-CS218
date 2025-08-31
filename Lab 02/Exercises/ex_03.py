# Insertion, Deletion, Searching - Tuple
import timeit

tpl = (23, 43, (5, 6), [], "Three")
tpl2 = (23, 43, (5, 6), [], "Three")

def custom_insert(data, pos):
    global tpl

    tuple_1 = tpl[:pos]
    tuple_2 = tpl[pos:]
    tuple_1 += (data,)

    tpl = tuple_1 + tuple_2

def custom_delete(data):
    global tpl

    for i in range(len(tpl)):
        if tpl[i] == data:
            tuple_1 = tpl[:i]
            tuple_2 = tpl[(i + 1):]
            tpl = tuple_1 + tuple_2
            return
    print("Data not found!")

def custom_search(data):
    global tpl

    for i in range(len(tpl)):
        if tpl[i] == data:
            return i
    return -1

# Main program
# Testing insertion
print("Insertion on first position:")
print("Original tuple1:", tpl)
exec_time_custom_insert = timeit.timeit(lambda: custom_insert(45, 0), number=1)
print("Final tuple1:", tpl)
print("Original tuple2:", tpl2)
exec_time_builtin_insert = timeit.timeit(lambda: tpl2.__add__((45,)), number=1)
print("Final tuple2:", tpl2 + (45,))
print("\nTime for custom insert:", exec_time_custom_insert)
print("Time for built-in insert:", exec_time_builtin_insert)
print("My function is so much slower than the built-in function:", exec_time_custom_insert / exec_time_builtin_insert)

# Testing deletion
print("\nDeletion:")
print("Original tuple1:", tpl)
exec_time_custom_delete = timeit.timeit(lambda: custom_delete(43), number=1)
print("Final tuple1:", tpl)
print("Original tuple2:", tpl2)
exec_time_builtin_delete = timeit.timeit(lambda: tuple(x for x in tpl2 if x != 43), number=1)
print("Final tuple2:", tuple(x for x in tpl2 if x != 43))
print("\nTime for custom delete:", exec_time_custom_delete)
print("Time for built-in delete:", exec_time_builtin_delete)
print("My function is so much slower than the built-in function:", exec_time_custom_delete / exec_time_builtin_delete)

# Testing searching
print("\nSearching for a key:")
print("Tuple1:", tpl)
exec_time_custom_search = timeit.timeit(lambda: custom_search((5, 6)), number=1)
print("Index found by custom search:", custom_search((5, 6)))
print("Tuple2:", tpl2)
exec_time_builtin_search = timeit.timeit(lambda: tpl2.index((5, 6)) if (5, 6) in tpl2 else -1, number=1)
print("Index found by built-in search:", tpl2.index((5, 6)) if (5, 6) in tpl2 else -1)
print("\nTime for custom search:", exec_time_custom_search)
print("Time for built-in search:", exec_time_builtin_search)
print("My function is so much slower than the built-in function:", exec_time_custom_search / exec_time_builtin_search)


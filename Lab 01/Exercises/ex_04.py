# Write a Python program to count the elements in a list until an element is a tuple. Note down the
# addresses of the tuple as well as the list.

my_list = [1, 2, 3, (4, 5), 6, 7]
print("Original list:", my_list)
print("Address of original list:", id(my_list), end='\n\n')

count = 0
for item in my_list:
    if isinstance(item, tuple):
        print("Tuple found:", item)
        print("Address of tuple:", id(item), end='\n\n')
        break
    count += 1
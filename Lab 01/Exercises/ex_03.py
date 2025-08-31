# Write down a python script to remove duplicates from the list. Note down the addresses of list
# before and after the removal of duplicates.

my_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", my_list)
print("Address of original list:", id(my_list), end='\n\n')

# First method
for item in my_list:
    while my_list.count(item) > 1:
        my_list.remove(item)

print("List after removing duplicates:", my_list)
print("Address of list after removing duplicates:", id(my_list), end='\n\n')

# Second method (alternative) <-- Creates a new list so address changes
new_list = []

for item in my_list:
    if item not in new_list:
        new_list.append(item)

print("New list after removing duplicates using alternative method:", new_list)
print("Address of new list:", id(new_list))
s = Stack(5)
print("Initial stack:", s.get_info())  # ( [None, None, None, None, None], -1 )

print("Performing push(10)")
s.push(10)
print("Performing push(20)")
s.push(20)
print("Stack after pushes:", s.get_info())  # ( [10, 20, None, None, None], 1 )

print("Performing pop()")
print("Popped item:", s.pop())       # 20
print("Stack after pop:", s.get_info())  # ( [10, 20, None, None, None], 0 )

print("Performing top()")
print("Top item:", s.top())       # 10

print("Checking if stack is empty:")
print(s.is_empty())  # False

print("Performing pop()")
s.pop()
print("Checking if stack is empty after pop:")
print(s.is_empty())  # True
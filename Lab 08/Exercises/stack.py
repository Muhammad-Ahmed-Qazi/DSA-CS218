class Stack:
    def __init__(self, max_size=10):
        self.items = [None for i in range(max_size)]
        self.tos = -1

    def get_info(self):
        return self.items, self.tos
    
    # A7.2 POP
    def pop(self):
        if self.tos == -1:
            raise IndexError("Underflow: Stack is empty!")
        item = self.items[self.tos]
        self.tos -= 1
        return item
    
    # A7.1 PUSH
    def push(self, item):
        if self.tos == len(self.items) - 1:
            raise IndexError("Overflow: Stack is full!")
        self.tos += 1
        self.items[self.tos] = item
    
    def top(self):
        if self.tos == -1:
            raise IndexError("Underflow: Stack is empty!")
        return self.items[self.tos]
    
    def is_empty(self):
        return self.tos == -1
    
    def display(self):
        stack = ''
        i = 0
        while i <= self.tos:
            stack += (str(self.items[i]) + ' ')
            i += 1
        
        return stack

# Main program
if __name__ == '__main__':
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
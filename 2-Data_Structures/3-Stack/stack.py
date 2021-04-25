from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        '''
        Constant time since the objects keep a reference to their lengths.
        '''
        return len(self.container)

    def print_stack(self):
        values = []
        for el in self.container:
            values.append(str(el))
        print('->'.join(values))


stack = Stack()

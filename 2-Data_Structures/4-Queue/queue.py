from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, value):
        self.container.append(value)

    def dequeue(self):
        try:
            return self.container.popleft()
        except:
            print('Nothing in the queue')
            return None

    def size(self):
        '''
        Constant time since the objects keep a reference to their lengths.
        '''
        return len(self.container)

    def print_queue(self):
        values = []
        for el in self.container:
            values.append(str(el))
        print('->'.join(values))


queue = Queue()

queue.dequeue()

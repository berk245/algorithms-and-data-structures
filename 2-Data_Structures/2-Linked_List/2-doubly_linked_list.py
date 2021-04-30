class DoublyNode:
    '''
    An object for storing a single node of a linked list
    Models three attributes - data and the links to the previous and next node in the list
    '''

    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None

    def __repr__(self):
        return '<Node data: %s>' % self.data


class DoublyLinkedList:
    '''
    Some methods that do not have major differences to singly_linked_list versions are omitted.
    To demonstrate differences, the reference to the tail is included in doubly linked list
    '''

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, data):
        '''
        - Adds a node as the new head of the list.
        - Takes constant time O(1)
        '''
        new_node = DoublyNode(data)

        if self.size:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1

    def insert(self, value, index):
        '''
        - Inserts a new Node containing data at index position
        - Insertion takes O(1) time
        - Finding the node at the insertion point takes O(n) time
        '''
        if index == 0:
            self.prepend(value)
            return

        current = self.head
        position = 0
        while current.next_node and position != index:
            current = current.next_node
            position += 1

        # We are now either at the index or at the end of the list
        to_insert = DoublyNode(value)

        prev = current.prev_node
        prev.next_node = to_insert
        to_insert.next_node = current
        to_insert.prev_node = prev
        current.prev_node = to_insert
        self.size += 1
        return

    def remove_value(self, key):
        '''
        - Finds a value and remove it form the list
        - Removing is O(1)
        - Finding the value to remove is O(n)
        '''
        if not self.size:
            return

        if key == self.head.data:
            self.head = self.head.next_node
            self.head.prev_node = None
            return
        elif key == self.tail.data:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            return

        current = self.head
        while current:
            if current.data == key:
                prev = current.prev_node
                nxt = current.next_node

                prev.next_node = nxt
                nxt.prev_node = prev
                print(current.data, ' removed')
                self.size -= 1
                return

            else:
                current = current.next_node
        print(key, 'not found')

    def remove_at_index(self, index):
        '''
        - Removes the node in the provided index
        - Removing is O(1)
        - Finding the value to remove is O(n)
        '''
        if index == 0:
            self.head = self.head.next_node
            self.head.prev_node = None
            return
        if index == self.size:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            return

        current = self.head
        position = 1
        try:
            while position != index:
                current = current.next_node
                position += 1
            # now current is the node to be deleted
            prev = current.prev_node
            nxt = current.next_node

            prev.next_node = nxt
            nxt.prev_node = prev

            print(current.data, 'is removed')
        except:
            print('Index not found')
            return

    def print_list(self):
        '''
        - Creates an array from the node data and prints them.
        - Takes linear Time
        '''
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        print(' -> '.join(result))


doubly = DoublyLinkedList()
doubly.prepend(1)
doubly.prepend(2)
doubly.prepend(3)
doubly.prepend(4)
doubly.prepend(5)
doubly.insert(3.5, 3)
doubly.print_list()
doubly.remove_value(4)
doubly.print_list()
doubly.remove_at_index(2)
doubly.print_list()

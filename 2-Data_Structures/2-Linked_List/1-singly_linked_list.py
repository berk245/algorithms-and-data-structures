class Node:
    '''
    An object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    '''

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return '<Node data: %s>' % self.data


class LinkedList:
    '''
    Singly linked list
    '''

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        '''
        - Returns the number of nodes in the list. 
        - Takes linear time
        '''
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def prepend(self, value):
        '''
        - Adds a node as the new head of the list.
        - Takes constant time O(1)
        '''
        new_node = Node(value)
        new_node.next_node = self.head

        self.head = new_node

    def search(self, key):
        '''
        - Searches for the first node that matches with the key.
        - Takes linear time O(n)
        '''
        current = self.head
        while current:
            if current.data == key:
                print(key, 'found')
                return
            else:
                current = current.next_node
        print(key, 'not found')

    def insert(self, data, index):
        '''
        - Inserts a new Node containing data at index position
        - Insertion takes O(1) time
        - Finding the node at the insertion point takes O(n) time
        '''
        if index == 0:
            self.prepend(data)
            return

        to_insert = Node(data)
        position = 1
        current = self.head

        while current.next_node and position != index:
            current = current.next_node
            position += 1

        to_insert.next_node = current.next_node

        current.next_node = to_insert

    def remove_value(self, value):
        '''
        - Finds a value and remove it form the list
        - Removing is O(1)
        - Finding the value to remove is O(n)
        '''
        current = self.head
        if current.data == value:
            self.head = current.next_node
            return

        while current:
            try:
                next_node = current.next_node
                if next_node.data == value:
                    try:
                        current.next_node = next_node.next_node
                        return
                    except:
                        current.next_node = None
                        return
                current = current.next_node
            except:
                print('Not found')
                return

    def remove_at_index(self, index):
        '''
        - Removes the node in the provided index
        - Removing is O(1)
        - Finding the value to remove is O(n)
        '''
        if index == 0:
            self.head = self.head.next_node
            return
        try:
            current = self.head
            position = 0
            while position != index - 1:
                current = current.next_node
                position += 1
            # now current is the node before the one to be deleted
            to_delete = current.next_node
            current.next_node = to_delete.next_node

            print(to_delete.data, 'is removed')
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


singly = LinkedList()
singly.prepend(1)
singly.prepend(2)
singly.prepend(3)
singly.prepend(4)
singly.prepend(5)
singly.prepend(6)
singly.insert(9, 12)
singly.print_list()
singly.remove_at_index(12)
singly.print_list()
singly.insert(7, 3)
singly.print_list()
singly.remove_value(9)
singly.print_list()

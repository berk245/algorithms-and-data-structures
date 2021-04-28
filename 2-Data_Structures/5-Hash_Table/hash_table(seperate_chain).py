class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        # Some hash function
        return 1

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        for element in self.arr[index]:
            # checks the items in the list, if the key is assigned before, it replaces the value
            if len(element) == 2 and element[0] == key:
                element[1] = value
                return
        # If the value has not been defined before, it appends it to the list.
        self.arr[index].append([key, value])

    def __getitem__(self, key):
        index = self.get_hash(key)
        for element in self.arr[index]:
            if element[0] == key:
                return element[1]


ht = HashTable()
ht['a'] = 6
ht['b'] = 5
ht['c'] = 2


print(ht.arr)

class HashTable:
    def __init__(self):
        self.MAX = 5
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        # Some hash function
        return 1

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        if not self.arr[index]:
            self.arr[index] = [key, value]
            return
        elif self.arr[index][0] == key:
            self.arr[index][1] == value
        else:
            for i in range(self.MAX):
                next_index = (index + i) % self.MAX
                if not self.arr[next_index]:
                    self.arr[next_index] = [key, value]
                    return
            raise Exception('No more space in the hash table')

    def __getitem__(self, key):
        index = self.get_hash(key)

        if self.arr[index][0] == key:
            return self.arr[index][1]
        else:
            for i in range(self.MAX):
                next_index = (index + i) % self.MAX
                if self.arr[next_index][0] == key:
                    return self.arr[next_index][1]
            print(key, 'Not Found')
            return


ht = HashTable()
ht['a'] = 6
ht['b'] = 5
ht['c'] = 2
ht['d'] = 2
ht['e'] = 2
ht['f'] = 2


print(ht.arr)

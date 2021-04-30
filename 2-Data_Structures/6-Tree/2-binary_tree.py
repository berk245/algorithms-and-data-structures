class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, new_data):
        if new_data < self.data:
            if self.left:
                self.left.add_child(new_data)
            else:
                self.left = BinarySearchTreeNode(new_data)
        elif new_data > self.data:
            if self.right:
                self.right.add_child(new_data)
            else:
                self.right = BinarySearchTreeNode(new_data)
        return

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, value):
        if value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        elif value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def in_order_traversal(self):
        ordered_elements = []
        # Go through left subtree
        if self.left:
            ordered_elements += self.left.in_order_traversal()
        # Add the base Node
        ordered_elements.append(self.data)
        # Go through right subtree
        if self.right:
            ordered_elements += self.right.in_order_traversal()
        return ordered_elements


root = BinarySearchTreeNode(20)


root.add_child(141)
root.add_child(11)
root.add_child(108)
root.add_child(12)
root.add_child(14)
root.add_child(123)
root.add_child(114)
print(root.in_order_traversal())
root.delete(12)

print(root.in_order_traversal())

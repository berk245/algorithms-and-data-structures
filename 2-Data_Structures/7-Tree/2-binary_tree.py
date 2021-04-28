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


root = BinarySearchTreeNode(15)

root.add_child(141)
root.add_child(11)
root.add_child(131)
root.add_child(11)
root.add_child(14)
root.add_child(123)

print(root.in_order_traversal())

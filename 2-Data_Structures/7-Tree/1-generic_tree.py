class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = self.get_level() * ' ' * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_a_sample_tree():
    root = TreeNode('Drinks')

    child1 = TreeNode('Beer')
    child1.add_child(TreeNode('Pilsener'))
    child1.add_child(TreeNode('Ale'))

    child2 = TreeNode('Whisky')
    child2.add_child(TreeNode('Single Malt'))
    child2.add_child(TreeNode('Irish'))

    child3 = TreeNode('Wine')
    child3.add_child(TreeNode('White'))
    child3.add_child(TreeNode('Red'))
    child3.add_child(TreeNode('Rose'))

    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)

    root.print_tree()


build_a_sample_tree()

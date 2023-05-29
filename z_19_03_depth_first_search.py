class Node():
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def pre_order(self, start, traversal_ls=None):

        if traversal_ls is None: traversal_ls = []
        if start is None:
            return

        traversal_ls.append(start.value)

        self.pre_order(start.left, traversal_ls)
        self.pre_order(start.right, traversal_ls)

        return traversal_ls

    def in_order(self, start, traversal_ls):
        if start is None:
            return

        self.in_order(start.left, traversal_ls)
        traversal_ls.append(start.value)
        self.in_order(start.right, traversal_ls)

        return traversal_ls

    def post_order(self, start, traversal_ls):
        if start is None:
            return

        self.post_order(start.left, traversal_ls)
        self.post_order(start.right, traversal_ls)
        traversal_ls.append(start.value)

        return traversal_ls


tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(tree.pre_order(tree.root,[]))
print(tree.in_order(tree.root,[]))
print(tree.post_order(tree.root,[]))
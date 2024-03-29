class Node():
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        if len(self.item):
            return self.item.pop(0)

    def peek(self):
        if len(self.item):
            return self.item[0].value


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def level_order(self, node):
        if node is None:
            return
        queue = Queue()
        queue.enqueue(node)
        traversal_ls = []
        while len(queue.item) > 0:
            traversal_ls.append(queue.peek())
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return traversal_ls


tree = BinaryTree(3)
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)
tree.root.left.left.left = Node(12)


tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)


tree.root.right.left.left = Node(11)

# print(tree.pre_order(tree.root, []))
# print(tree.in_order(tree.root, []))
# print(tree.post_order(tree.root, []))

print(tree.level_order(tree.root))
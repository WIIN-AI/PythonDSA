class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_right_left(self.root, value)

    def _add_right_left(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_right_left(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_right_left(node.right, value)

    def print_node_value(self):
        self._traverse_inorder_(self.root)

    def _traverse_inorder_(self, node):
        if node is not None:
            print(node.value, end="-->")
            self._traverse_inorder_(node.left)
            self._traverse_inorder_(node.right)
            # print(node.value, end="**")

    def fn_search(self, value):
        return self._recursive_search(self.root, value,count=0)

    def _recursive_search(self, node, value,count=0):

        if node is None or node.value == value:
            return count

        if value < node.value:
            return self._recursive_search(node.left, value, count+1)
        else:
            return self._recursive_search(node.right, value,count+1)


# binaryTree = BinaryTree(4)
# binaryTree.root.left = Node(5)
# binaryTree.root.left.left = Node(6)
# binaryTree.root.left.right = Node(7)
#
# binaryTree.root.right = Node(6)
# binaryTree.root.right.left = Node(8)
# binaryTree.root.right.right = Node(9)

binarytree = BinaryTree()
binarytree.add(11)
binarytree.add(12)
binarytree.add(7)
binarytree.add(5)
binarytree.add(6)
binarytree.add(1)

binarytree.print_node_value()
# result = binarytree.fn_search(5)
# print("result",result)
# if result:
#     print("Value 5 is found in the tree.")

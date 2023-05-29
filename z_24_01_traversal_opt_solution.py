class Node():
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class Solution:

    def __init__(self):
        self.start = None

    def build_tree(self, pre_order, in_order):
        memory = {}
        for i, e in enumerate(in_order):
            memory[e] = i

        self.helper(pre_order[::-1], in_order, left_pointer=0, right_pointer=len(in_order), memory=memory)

    def helper(self, pre_order, in_order, left_pointer, right_pointer, memory):
        if left_pointer > right_pointer: return None
        num = pre_order.pop()
        root = Node(num)
        idx = memory.get(num)

        root.left = self.helper(pre_order, in_order, left_pointer, idx, memory)
        root.right = self.helper(pre_order, in_order, idx + 1, right_pointer, memory)

        return root

    def print_pre_order(self, start, traversal_ls):
        """
         ROOT --> LEFT --> RIGHT
        :param start: start node or ROOT NODE
        :param traversal_ls: []
        :return: entire traversal list
        """
        if start is None:
            return

        traversal_ls.append(start.value)
        self.print_pre_order(start.left, traversal_ls)
        self.print_pre_order(start.right, traversal_ls)

        return traversal_ls

    def print_in_order(self, start, traversal_ls):
        """
            LEFT --> ROOT --> RIGHT

        :param start: start node or ROOT NODE
        :param traversal_ls: []
        :return: entire traversal list
        """

        if start is None:
            return

        self.print_in_order(start.left, traversal_ls)
        traversal_ls.append(start.value)
        self.print_in_order(start.right, traversal_ls)

        return traversal_ls

    def print_post_order(self, start, traversal_ls):
        """
        LEFT --> RIGHT --> ROOT
        :param start: start node or ROOT NODE
        :param traversal_ls: []
        :return: entire traversal list
        """
        if start is None:
            return

        self.print_post_order(start.left, traversal_ls)
        self.print_post_order(start.right, traversal_ls)
        traversal_ls.append(start.value)

        return traversal_ls


pre_order_ls = [3, 9, 20, 15, 7]
in_order_ls = [9, 3, 15, 20, 7]

sol = Solution()
start_node = sol.build_tree(pre_order_ls, in_order_ls)
print(start_node.value)
print(start_node.left)
print(start_node.right)

print(sol.print_pre_order(start_node, []))
print(sol.print_in_order(start_node, []))
print(sol.print_post_order(start_node, []))

class Node():
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None


class Solution:

    def __init__(self):
        self.start = None

    def build_tree(self, pre_order, in_order):
        if len(in_order) == 0:
            return None

        if len(pre_order) == 1:
            last_node = Node(pre_order[0])
            return last_node

        root_index = in_order.index(pre_order.pop(0))
        node = Node(in_order[root_index])
        node.left = self.build_tree(pre_order, in_order[:root_index])
        node.right = self.build_tree(pre_order, in_order[root_index + 1:])

        self.start = node
        return node

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

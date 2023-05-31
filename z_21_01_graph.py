class Node:
    def __init__(self, value):
        self.adjacent_ls = []
        self.value = value
        self.visited = False


class Graph:

    def bfs(self, node):
        queue_f = []
        queue_f.append(node)
        node.visited = True

        traversal = []

        while queue_f:
            actualNode = queue_f.pop(0)
            traversal.append(actualNode.value)
            for element in actualNode.adjacent_ls:
                if element.visited is False:
                    queue_f.append(element)
                    element.visited = True

        return traversal

    def dfs(self, node, traversal=[]):
        node.visited = True
        traversal.append(node.value)
        for element in node.adjacent_ls:
            if element.visited is False:
                self.dfs(element, traversal)

        return traversal


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")
# node8 = Node("I")
# node8 = Node("J")


node1.adjacent_ls.append(node2)
node1.adjacent_ls.append(node3)
node1.adjacent_ls.append(node4)

node2.adjacent_ls.append(node5)
node2.adjacent_ls.append(node6)

node4.adjacent_ls.append(node7)
node6.adjacent_ls.append(node8)

# graph = Graph()
# print(graph.bfs(node1))

# graph = Graph()
# print(graph.dfs(node1))

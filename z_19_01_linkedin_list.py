class Node():
    def __init__(self, value):
        self.prev = None
        self.val = value
        self.next = None


class LinkedIs():
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next

            new_node.prev = temp_node
            temp_node.next = new_node

    def print_nodes(self):

        node = self.head
        while node is not None:
            print(node.val)
            node = node.next


LiLs = LinkedIs()
LiLs.add(10)
LiLs.add(15)
LiLs.print_nodes()

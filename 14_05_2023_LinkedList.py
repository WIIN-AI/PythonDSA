
class Node():
    def __init__(self ,value):
        self.value = value
        self.next =None


class LinkedList():
    def __init__(self):
        self.head = None

    @staticmethod
    def print_fn():
        print("General print ")

    def insert_node(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def add_node_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head  # first assigning the value head to new node next
        self.head = new_node  # shifting the head to new node

    def print_elements (self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


# Create a new linked list
my_list = LinkedList()

# Insert elements
my_list.add_node_at_first(5)
my_list.add_node_at_first(10)
my_list.insert_node(15)
my_list.print_elements()  # Output: [10, 5, 15]

# # Search for an element
# print(my_list.search(10))  # Output: True
# print(my_list.search(20))  # Output: False

# # Delete an element
# my_list.delete(5)
# my_list.display()  # Output: [10, 15]
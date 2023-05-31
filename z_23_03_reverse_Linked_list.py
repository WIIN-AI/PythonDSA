class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index_val):
        current_node = self.head
        counter = 0
        while counter != index_val:
            current_node = current_node.next
            counter += 1
        print()
        print(current_node.value)

    def add_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            new_node.prev = current_node
            current_node.next = new_node

    def delete_node(self, value):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.value == value:
                if prev_node is None:
                    self.head = current_node.next
                else:
                    prev_node.next = current_node.next

                # let say if we found duplicate values in linked list
                prev_node = current_node  # This become head after one iteration
                current_node = current_node.next  #
            else:
                prev_node = current_node  # This become head after one iteration
                current_node = current_node.next  #

        print(f"Node with value {value} not found in the list.")

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("END")

    def display_reverse(self, head):
        current_node = head
        previous = None
        next_node = None

        while current_node:
            next_node = current_node.next  # get the next of next value
            current_node.next = previous  # None

            previous = current_node  # adding to
            current_node = next_node

        head = previous

        new_node = head
        while new_node:
            print(new_node.value)
            new_node = new_node.next

    def prac_reverse(self, head):
        prev = None
        current = head
        current_to_next_node = None

        while current:
            next_node = current.next # next node for iteration

            current.next = prev
            prev = current

            current = next_node # assigning back to holder current point

        head = prev
        return head


my_list = LinkedList()

# Append elements
my_list.add_node(10)
my_list.add_node(20)
my_list.add_node(30)
my_list.add_node(40)

# Display the original list
print("Original list:")
my_list.display()

# Delete a node
my_list.delete_node(20)

# Display the updated list
print("List after deletion:")
my_list.display()

my_list.get(1)

my_list.add_at_head(50)

my_list.display()
my_list.display_reverse(my_list.head)

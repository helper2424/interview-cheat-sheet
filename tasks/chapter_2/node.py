class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_node(self, value):
        current_node = self
        while current_node.next != None:
            current_node = current_node.next

        current_node.next = Node(value)
        return current_node

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def delete(self, index):
        if index < 0:
            return  # Invalid index

        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        prev = None
        for _ in range(index):
            prev = current_node
            if current_node.next is None:
                return  # Index out of bounds
            current_node = current_node.next

        prev.next = current_node.next

    def __str__(self):
        s = ''
        node = self.head
        while node is not None:
            s += node.data
            node = node.next
        return s if s else "Empty list"



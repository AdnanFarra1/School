class Node:
    def __init__(self, data=None):
        self.data = data
        self.pointer = None
class linked_list:
    def __init__(self):
        self.Head = Node()
    def append(self, data):
        new_node = Node(data)
        current_node = self.Head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    def length(self):
        current_node = self.Head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total

    
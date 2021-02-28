class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_children(self, node):
        self.children.append(node)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    def insert(self, node, data):
        if node is None:
            self.createNode(data )
        if data > node.data:
            self.insert(node.right)
        elif data < node.data:
            self.insert(node.right)



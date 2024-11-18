class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if not self.root:
            self.root = Node(key, data)
        else:
            self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if key < node.key:
            if node.left:
                self._insert(node.left, key, data)
            else:
                node.left = Node(key, data)
        elif key > node.key:
            if node.right:
                self._insert(node.right, key, data)
            else:
                node.right = Node(key, data)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            self._search(node.left, key)
        else:
            self._search(node.right, key)

    def print_all(self):
        self._print(self.root)

    def _print(self, node=None):
        if not node:
            print('Empty')
        else:
            print(node.data)
            if node.left:
                self._print(node.left)
            if node.right:
                self._print(node.right)
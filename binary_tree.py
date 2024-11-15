class Node:
    def __init__(self, key, person):
        self.key = key
        self.person = person
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, person):
        if not self.root:
            self.root = Node(key, person)
        else:
            self._insert(self.root, key, person)

    def _insert(self, node, key, person):
        if key < node.key:
            if node.left:
                self._insert(node.left, key, person)
            else:
                node.left = Node(key, person)
        elif key > node.key:
            if node.right:
                self._insert(node.right, key, person)
            else:
                node.right = Node(key, person)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.person
        elif key < node.key:
            self._search(node.left, key)
        else:
            self._search(node.right, key)

    def print_all(self):
        return self._print(self.root)

    def _print(self, node=None):
        if not node:
            print('Empty')
        else:
            print(node.person)
            if node.left:
                self._print(node.left)
            if node.right:
                self._print(node.right)
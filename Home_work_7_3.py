class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.value + self._sum_values(node.left) + self._sum_values(node.right)

# Приклад використання
bst = BinarySearchTree()
values = [20, 10, 30, 5, 15, 25, 35]

for value in values:
    bst.insert(value)

print("Сума всіх значень у дереві:", bst.sum_values())

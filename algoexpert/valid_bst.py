# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    def helper(node, min_node, max_node):
        if node is None:
            return True
        if min_node and node.value < min_node.value:
            return  False
        if max_node and node.value >= max_node.value:
            return False
        return helper(node.left, min_node, node) and helper(node.right, node, max_node)
    return helper(tree, None, None)


#  https://leetcode.com/problems/binary-search-tree-iterator/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stk = []
        self.inOrder(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stk) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stk.pop()
        self.inOrder(node.right)
        return node.val

    def inOrder(self, node):
        while node:
            self.stk.append(node)
            node = node.left


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(10)

    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    print v

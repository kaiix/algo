#  https://leetcode.com/problems/invert-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def invertTree(root):
    if not root:
        return root
    left_child = root.left
    right_child = root.right
    root.left = invertTree(right_child)
    root.right = invertTree(left_child)
    return root


def printTree(root):
    stk = [root]
    while stk:
        node = stk.pop(0)
        print node.val
        if node.left:
            stk.append(node.left)
        if node.right:
            stk.append(node.right)

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    printTree(invertTree(root))

#  https://leetcode.com/problems/sum-root-to-leaf-numbers/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sumNumbers(root):
    if not root:
        return 0
    elif root.left is None and root.right is None:
        return root.val
    else:
        if root.left:
            root.left.val += root.val * 10
        if root.right:
            root.right.val += root.val * 10
        return sumNumbers(root.left) + sumNumbers(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print sumNumbers(root)

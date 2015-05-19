#  https://leetcode.com/problems/path-sum/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def hasPathSum(root, sum):
    if not root:
        return False
    elif root.left is None and root.right is None:
        return sum == root.val
    else:
        left, right = False, False
        if root.left:
            left = hasPathSum(root.left, sum-root.val)
        if root.right:
            right = hasPathSum(root.right, sum-root.val)
        return left or right


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    print hasPathSum(root, 22)

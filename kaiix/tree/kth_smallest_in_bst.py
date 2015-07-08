#  https://leetcode.com/problems/kth-smallest-element-in-a-bst/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def kthSmallest(root, k):
    result = []
    flatten(root, result)
    return result[k-1]


def flatten(root, result):
    if root:
        flatten(root.left, result)
        result.append(root.val)
        flatten(root.right, result)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(10)

    for k in xrange(1, 8):
        print kthSmallest(root, k)

#  https://leetcode.com/problems/path-sum-ii/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def pathSum(root, sum):
    if not root:
        return []
    elif root.left is None and root.right is None:
        if sum == root.val:
            return [[sum]]
        else:
            return []
    else:
        result = []
        left = pathSum(root.left, sum-root.val)
        for path in left:
            path.insert(0, root.val)
            result.append(path)
        right = pathSum(root.right, sum-root.val)
        for path in right:
            path.insert(0, root.val)
            result.append(path)
        return result


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    print pathSum(root, 22)

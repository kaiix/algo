class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def zigzagLevelOrder(root):
    if root is None:
        return []

    level = [root]
    forward = True
    result = []
    while level:
        it = iter(level) if forward else reversed(level)
        result.append(map(lambda x: x.val, it))
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        forward = not forward
    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    print zigzagLevelOrder(root)

#  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def buildTree(inorder, postorder):
    if not inorder:
        return None

    root = TreeNode(postorder.pop())
    if not postorder:
        return root

    idx = inorder.index(root.val)
    left = inorder[:idx]
    right = inorder[idx+1:]

    if postorder[-1] in left:
        root.left = buildTree(left, postorder)
        root.right = buildTree(right, postorder)
    else:
        root.right = buildTree(right, postorder)
        root.left = buildTree(left, postorder)
    return root


def printTree(root):
    stk = [root]
    while stk:
        node = stk.pop(0)
        if node:
            print node.val
            stk.append(node.left)
            stk.append(node.right)


if __name__ == '__main__':
    printTree(buildTree([5], [5]))
    printTree(buildTree([1, 2], [2, 1]))
    printTree(buildTree([1, 2, 5, 7, 6, 8, 4], [2, 1, 6, 7, 4, 8, 5]))

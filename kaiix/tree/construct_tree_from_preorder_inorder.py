#  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def buildTree(preorder, inorder):
    if not inorder:
        return None

    root = TreeNode(preorder.pop(0))
    if not preorder:
        return root

    idx = inorder.index(root.val)
    left = inorder[:idx]
    right = inorder[idx+1:]

    if preorder[0] in left:
        root.left = buildTree(preorder, left)
        root.right = buildTree(preorder, right)
    else:
        root.right = buildTree(preorder, right)
        root.left = buildTree(preorder, left)
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
    printTree(buildTree([1, 2, 3, 4, 5, 6], [3, 2, 4, 5, 1, 6]))

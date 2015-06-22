#  https://leetcode.com/problems/unique-binary-search-trees-ii/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generateTrees(n):
    return generateTreesInRange(1, n)


def generateTreesInRange(b, e):
    if b > e:
        return [None]
    if b == e:
        return [TreeNode(b)]
    result = []
    for r in xrange(b, e+1):
        left = generateTreesInRange(b, r-1)
        right = generateTreesInRange(r+1, e)
        for lhs in left:
            for rhs in right:
                root = TreeNode(r)
                root.left = lhs
                root.right = rhs
                result.append(root)
    return result


def printTree(root):
    stk = [root]
    while stk:
        node = stk.pop(0)
        print node.val
        if node.left:
            stk.append(node.left)
        if node.right:
            stk.append(node.right)
    print '=' * 10


if __name__ == '__main__':
    trees = generateTrees(3)
    for t in trees:
        printTree(t)

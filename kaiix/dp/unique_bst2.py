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


def generateTreesDP(n):
    if n <= 0:
        return [[]]

    dp = [[[] for x in xrange(n)] for x in xrange(n)]
    for i in xrange(n):
        dp[i][i].append(TreeNode(i+1))
    for i in reversed(xrange(n)):
        for j in xrange(i+1, n):
            for r in xrange(i, j+1):
                if r-1 < i:
                    left = [None]
                else:
                    left = dp[i][r-1]
                if r+1 > j:
                    right = [None]
                else:
                    right = dp[r+1][j]
                for lhs in left:
                    for rhs in right:
                        t = TreeNode(r+1)
                        t.left = lhs
                        t.right = rhs
                        dp[i][j].append(t)
    return dp[0][-1]


def printTree(root):
    stk = [root]
    while stk:
        node = stk.pop(0)
        if node:
            print node.val,
        else:
            print '#',
        if node:
            stk.append(node.left)
            stk.append(node.right)
    print


if __name__ == '__main__':
    trees = generateTrees(3)
    for t in trees:
        printTree(t)

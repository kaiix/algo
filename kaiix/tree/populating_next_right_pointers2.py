#  https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def connect(root):
    if not root:
        return

    s = [root]
    while s:
        for i in xrange(len(s)):
            if i+1 >= len(s):
                s[i].next = None
            else:
                s[i].next = s[i+1]
        for i in xrange(len(s)):
            n = s.pop(0)
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
    return root


def printTree(root):
    s = [root]
    while s:
        n = s.pop(0)
        if n.left:
            s.append(n.left)
        while n:
            print n.val
            n = n.next


if __name__ == '__main__':
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.right = TreeLinkNode(7)

    printTree(connect(root))

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmetricIterative(root.left, root.right)

    def isSymmetricRecursive(self, left, right):
        if not left:
            if not right:
                return True
            return False
        if not right:
            return False
        if left.val != right.val:
            return False
        if not self.isSymmetricRecursive(left.left, right.right):
            return False
        if not self.isSymmetricRecursive(left.right, right.left):
            return False
        return True

    def isSymmetricIterative(self, left, right):
        qleft = [left]
        qright = [right]
        while qleft:
            if not qright:
                return False
            l = qleft.pop(0)
            r = qright.pop(0)
            if not l and not r:
                continue
            if (not l and r) or (l and not r) or (l.val != r.val):
                return False
            qleft.append(l.left)
            qright.append(r.right)
            qleft.append(l.right)
            qright.append(r.left)
        if qright:
            return False
        return True

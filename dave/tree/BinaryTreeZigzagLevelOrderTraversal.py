# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        q = [[root]]
        ret = []
        d = True
        while q:
            l = q.pop(0)
            v = []
            ll = []
            for n in l:
                if n:
                    v.append(n.val)
                    ll.append(n.left)
                    ll.append(n.right)
            d = not d
            if d:
                v.reverse()
            if v:
                ret.append(v)
            if ll:
                q.append(ll)
        return ret

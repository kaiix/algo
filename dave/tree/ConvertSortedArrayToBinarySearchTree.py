# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        return self._sortedArrayToBST(num, 0, len(num))

    def _sortedArrayToBST(self, num, begin, end):
        if begin >= end or not num:
            return None
        mid = (end - begin) / 2 + begin
        node = TreeNode(num[mid])
        node.left = self._sortedArrayToBST(num, begin, mid)
        node.right = self._sortedArrayToBST(num, mid + 1, end)
        return node

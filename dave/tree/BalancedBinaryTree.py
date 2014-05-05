# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.balancedHeight(root) >= 0

    def balancedHeight(self, root):
        if not root:
            return 0
        left = self.balancedHeight(root.left)
        right = self.balancedHeight(root.right)
        if left < 0 or right < 0:
            return -1
        if left - right > 1 or right - left > 1:
            return -1
        return max(left, right) + 1

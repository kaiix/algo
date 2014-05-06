# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return None
        if root.right:
            self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            tail = root.left
            while tail.right:
                tail = tail.right
            tmp = root.right
            root.right = root.left
            root.left = None
            tail.right = tmp

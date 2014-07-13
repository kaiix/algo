# https://oj.leetcode.com/problems/search-insert-position/


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        p = 0
        while p < len(A) and target > A[p]:
            p += 1
        return p

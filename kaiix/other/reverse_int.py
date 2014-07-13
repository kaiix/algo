# https://oj.leetcode.com/problems/reverse-integer/


class Solution:
    # @return an integer
    def reverse(self, x):
        return int(''.join(map(lambda s: s[::-1], str(x).rpartition('-'))))

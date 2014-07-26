# https://oj.leetcode.com/problems/climbing-stairs/

memo = {}


def memoization(meth):
    def _meth(self, n):
        if memo.get(n) is None:
            memo[n] = meth(self, n)
        return memo[n]
    return _meth


class Solution:
    # @param n, an integer
    # @return an integer
    @memoization
    def climbStairs(self, n):
        if n <= 3:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

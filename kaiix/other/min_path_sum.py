#  https://leetcode.com/problems/minimum-path-sum/


class Solution:
    memoize = {}

    def minPathSum(self, grid):
        self.memoize = {}
        return self._minPathSum(grid, len(grid)-1, len(grid[0])-1)

    def _minPathSum(self, grid, i, j):
        if self.memoize.get((i, j)):
            return self.memoize[(i, j)]

        if i < 0 or j < 0:
            return None
        else:
            self.memoize[(i-1, j)] = self._minPathSum(grid, i-1, j)
            self.memoize[(i, j-1)] = self._minPathSum(grid, i, j-1)
            if self.memoize[(i-1, j)] is None or self.memoize[(i, j-1)] is None:
                minval = self.memoize[(i-1, j)] or self.memoize[(i, j-1)]
                minval = minval or 0
            else:
                minval = min(self.memoize[(i-1, j)], self.memoize[(i, j-1)])
            return grid[i][j] + minval


if __name__ == '__main__':
    print Solution().minPathSum([
        [8, 3, 2],
    ])

    print Solution().minPathSum([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ])

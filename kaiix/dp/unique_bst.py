#  https://leetcode.com/problems/unique-binary-search-trees/


def numTrees2(n):
    return numTreesInRange(1, n)


def numTreesInRange(start, end):
    if start >= end:
        return 1

    num = 0
    for root in xrange(start, end+1):
        num += numTreesInRange(start, root-1) * numTreesInRange(root+1, end)
    return num


def numTrees(n):
    dp = [[1] * n for x in xrange(n)]
    for i in reversed(xrange(n)):
        for j in xrange(i+1, n):
            num = 0
            for r in xrange(i, j+1):
                if r-1 <= i:
                    left = 1
                else:
                    left = dp[i][r-1]
                if r+1 >= j:
                    right = 1
                else:
                    right = dp[r+1][j]
                num += left * right
            dp[i][j] = num
    return dp[0][-1]


if __name__ == '__main__':
    for i in xrange(1, 10):
        print numTrees(i)
        print numTrees2(i)

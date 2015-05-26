#  https://leetcode.com/problems/triangle/


cache = {}


def minimumTotalRecursive(triangle):
    global cache
    cache = {}
    m = None
    for i in xrange(len(triangle[-1])):
        leaf = _minimumTotal(triangle, len(triangle)-1, i)
        if m is None or leaf < m:
            m = leaf
    return m


def _minimumTotal(triangle, i, j):
    if cache.get((i, j)):
        return cache[(i, j)]

    if i == 0 and j == 0:
        return triangle[i][j]

    if j == 0:
        minimum = _minimumTotal(triangle, i-1, j)
    elif j == i:
        minimum = _minimumTotal(triangle, i-1, j-1)
    else:
        minimum = min(_minimumTotal(triangle, i-1, j),
                      _minimumTotal(triangle, i-1, j-1))
    cache[(i, j)] = triangle[i][j] + minimum
    return cache[(i, j)]


def minimumTotal(triangle):
    dp = []
    for i in xrange(len(triangle)):
        row = []
        for j in xrange(len(triangle[i])):
            if i == 0 and j == 0:
                m = 0
            elif j == 0:
                m = dp[i-1][j]
            elif j == i:
                m = dp[i-1][j-1]
            else:
                m = min(dp[i-1][j-1], dp[i-1][j])
            row.append(triangle[i][j]+m)
        dp.append(row)
    return min(dp[-1])


if __name__ == '__main__':
    print minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])

    print minimumTotal([
        [1],
        [2, 3],
    ])

    print minimumTotal([
        [-1],
        [2, 3],
        [1, -1, -1],
    ])

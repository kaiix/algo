#  https://leetcode.com/problems/unique-paths/

memoize = {}


def uniquePaths(m, n):
    if memoize.get((m, n)):
        return memoize[(m, n)]

    if m < 1:
        return 0
    elif n < 1:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        if not memoize.get((m-1, n)):
            memoize[(m-1, n)] = uniquePaths(m-1, n)
        if not memoize.get((m, n-1)):
            memoize[(m, n-1)] = uniquePaths(m, n-1)
        return memoize[(m-1, n)] + memoize[(m, n-1)]


if __name__ == '__main__':
    print uniquePaths(3, 7)
    print uniquePaths(23, 12)

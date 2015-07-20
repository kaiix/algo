#  https://leetcode.com/problems/set-matrix-zeroes/


def setZeros(matrix):
    m, n = len(matrix), len(matrix[0])
    r = [False] * m  # rows contain zeros
    c = [False] * n
    for i in xrange(m):
        for j in xrange(n):
            if matrix[i][j] == 0:
                r[i] = True
                c[j] = True
    for i, is_zero in enumerate(r):
        if is_zero:
            for j in xrange(n):
                matrix[i][j] = 0
    for j, is_zero in enumerate(c):
        if is_zero:
            for i in xrange(m):
                matrix[i][j] = 0


if __name__ == '__main__':
    import pprint
    matrix = [[1, 1, 1],
              [1, 0, 1]]
    setZeros(matrix)
    pprint.pprint(matrix)

#  https://leetcode.com/problems/spiral-matrix-ii/


def generateMatrix2(n):
    result = [[0 for _ in xrange(n)] for _ in xrange(n)]

    hr, inc = True, True
    x, length = 1, n*n+1
    i, j = 0, 0
    while x < length:
        result[i][j] = x
        x += 1

        if hr and inc:
            if j == n-1 or result[i][j+1] > 0:
                hr, inc = False, True
        elif not hr and inc:
            if i == n-1 or result[i+1][j] > 0:
                hr, inc = True, False
        elif hr and not inc:
            if j == 0 or result[i][j-1] > 0:
                hr, inc = False, False
        else:
            if i == 0 or result[i-1][j] > 0:
                hr, inc = True, True

        if hr and inc:
            j += 1
        elif not hr and inc:
            i += 1
        elif hr and not inc:
            j -= 1
        else:
            i -= 1

    return result


# slower
def generateMatrix(n):
    matrix = [[0 for _ in xrange(n)] for _ in xrange(n)]
    i, j, k = 0, 0, 0
    while k < n*n:
        while j < n-i:
            k += 1
            matrix[i][j] = k
            j += 1
        i += 1
        j -= 1
        while i <= j:
            k += 1
            matrix[i][j] = k
            i += 1
        i -= 1
        j -= 1
        while j >= n-i-1:
            k += 1
            matrix[i][j] = k
            j -= 1
        i -= 1
        j += 1
        while i > j:
            k += 1
            matrix[i][j] = k
            i -= 1
        i += 1
        j += 1
    return matrix


def printMatrix(matrix):
    for row in matrix:
        print '[{}]'.format(', '.join(map(lambda x: '{:0>2d}'.format(x), row)))

if __name__ == '__main__':
    printMatrix(generateMatrix(5))

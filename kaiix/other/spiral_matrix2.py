#  https://leetcode.com/problems/spiral-matrix-ii/


def generateMatrix(n):
    result = [[0 for _ in xrange(n)] for _ in xrange(n)]
    hr, inc = True, True
    x, length = 1, n*n+1
    i, j = 0, 0
    while x < length:
        result[i][j] = x
        x += 1

        if hr and inc:
            if j == n-1 or result[i][j+1] > 0:
                hr = False
                inc = True
        elif not hr and inc:
            if i == n-1 or result[i+1][j] > 0:
                hr = True
                inc = False
        elif hr and not inc:
            if j == 0 or result[i][j-1] > 0:
                hr = False
                inc = False
        elif not hr and not inc:
            if i == 0 or result[i-1][j] > 0:
                hr = True
                inc = True

        if hr and inc:
            j += 1
        elif not hr and inc:
            i += 1
        elif hr and not inc:
            j -= 1
        else:
            i -= 1
    return result


def printMatrix(matrix):
    for row in matrix:
        print row

if __name__ == '__main__':
    printMatrix(generateMatrix(5))

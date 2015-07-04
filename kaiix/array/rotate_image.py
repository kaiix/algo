#  https://leetcode.com/problems/rotate-image/


def rotate(matrix):
    return rotateRecursive(matrix, 0, len(matrix))


    def rotateRecursive(matrix, offset, dimen):
        if dimen <= 1:
            return

        top = matrix[offset][:]
        for i in xrange(dimen):
            matrix[offset][offset+dimen-1-i] = matrix[offset+i][offset]
        for i in xrange(dimen):
            matrix[offset+i][offset] = matrix[offset+dimen-1][offset+i]
        for i in xrange(dimen):
            matrix[offset+dimen-1][offset+i] = matrix[offset+dimen-1-i][offset+dimen-1]
        for i in xrange(dimen):
            matrix[offset+i][offset+dimen-1] = top[offset+i]
        rotateRecursive(matrix, offset+1, dimen-2)


def printMatrix(matrix):
    n = len(matrix)
    for row in xrange(n):
        print matrix[row]


if __name__ == '__main__':
    for m in [
        [[1]],
        [[1, 2], [4, 3]],
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
        [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
    ]:
        rotate(m)
        printMatrix(m)
        print '='*20

#  https://leetcode.com/problems/spiral-matrix/


def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    w, h = len(matrix[0]), len(matrix)
    i, j, k = 0, 0, 0
    while k < h and k < w:
        c = 0
        while c < w-k:
            result.append(matrix[i][j])
            j += 1
            c += 1
        j -= 1
        i += 1
        c = 0
        while c < h-k-1:
            result.append(matrix[i][j])
            i += 1
            c += 1
        i -= 1
        j -= 1
        c = 0
        k += 1
        if k >= h or k >= w:
            break
        while c < w-k:
            result.append(matrix[i][j])
            j -= 1
            c += 1
        j += 1
        i -= 1
        c = 0
        while c < h-k-1:
            result.append(matrix[i][j])
            i -= 1
            c += 1
        i += 1
        j += 1
        k += 1
    return result


if __name__ == '__main__':
    print spiralOrder(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )

#  https://leetcode.com/problems/search-a-2d-matrix/


def searchMatrix(matrix, target):
    rl, rh = 0, len(matrix)-1
    while rl <= rh:
        mid = (rl + rh) / 2
        if matrix[mid][0] > target:
            rh = mid-1
        elif matrix[mid][0] < target:
            if matrix[mid][-1] > target:
                return searchRow(matrix[mid], target)
            elif matrix[mid][-1] == target:
                return True
            else:
                rl = mid+1
        else:
            return True
    return False


def searchRow(row, target):
    low, high = 0, len(row)-1
    while low <= high:
        mid = (low + high) / 2
        if row[mid] > target:
            high = mid-1
        elif row[mid] < target:
            low = mid+1
        else:
            return True
    return False


if __name__ == '__main__':
    print searchMatrix(
        [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ],
        3
    )

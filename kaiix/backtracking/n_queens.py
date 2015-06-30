#  https://leetcode.com/problems/n-queens/


def findPlace(row, start, board):
    for col in xrange(start, len(board)):
        if canPlace(row, col, board):
            return col
    return -1


def canPlace(row, col, board):
    n = len(board)
    for r in reversed(xrange(row)):
        if (board[r] == col
            or ((col-row+r >= 0) and board[r] == col-row+r)
            or ((col+row-r < n) and board[r] == col+row-r)):
            return False
    return True


def printBoard(board):
    printed = [bytearray('.'*len(board)) for _ in xrange(len(board))]
    for row, col in enumerate(board):
        printed[row][col] = 'Q'
    return map(str, printed)


def solveNQueens(n):
    result = []
    row, col, start = 0, 0, 0
    board = [-1] * n
    while row >= 0 and row < n:
        col = findPlace(row, start, board)
        if col >= 0:
            board[row] = col
            if row == n-1 and board[-1] >= 0:
                result.append(printBoard(board[:]))
                row -= 1
                start = board[row] + 1
            else:
                col = board[row] + 1
                row += 1
                start = 0
        else:
            row -= 1
            start = board[row] + 1

    return result


if __name__ == '__main__':
    import pprint
    for i in xrange(6):
        pprint.pprint(solveNQueens(i))

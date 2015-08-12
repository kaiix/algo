#  https://leetcode.com/problems/n-queens-ii/


def totalNQueens(n):
    return len(n_queens(n))


def n_queens(n):
    result = []
    board = [-1] * n
    for i in xrange(n):
        solve_n_queens(0, i, n, board, result)
    return result


def can_place(col, row, n, board):
    for i in reversed(xrange(col)):
        offset = col - i
        if (board[i] == row
            or (row-offset >= 0 and board[i] == row-offset)
            or (row+offset < n and board[i] == row+offset)):
            return False
    return True


def solve_n_queens(col, row, n, board, result):
    if can_place(col, row, n, board):
        board[col] = row
        if col == n-1:
            result.append(board[:])
        else:
            for i in xrange(n):
                solve_n_queens(col+1, i, n, board, result)


if __name__ == '__main__':
    print totalNQueens(8)

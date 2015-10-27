#  https://leetcode.com/problems/nim-game/


def canWinNim(n):
    if n <= 3:
        return True
    else:
        return n % 4 != 0


if __name__ == '__main__':
    for i in xrange(1, 20):
        if not canWinNim(i):
            print i

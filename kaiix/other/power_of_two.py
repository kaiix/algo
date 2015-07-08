#  https://leetcode.com/problems/power-of-two/


def isPowerOfTwo(n):
    if n == 0:
        return False
    if n == 1:
        return True

    if n % 2:
        return False
    else:
        return isPowerOfTwo(n/2)

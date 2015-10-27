#  https://leetcode.com/problems/ugly-number/


def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0:
        return False
    if num == 1:
        return True
    if num % 2 == 0:
        return isUgly(num/2)
    elif num % 3 == 0:
        return isUgly(num/3)
    elif num % 5 == 0:
        return isUgly(num/5)
    else:
        return False


if __name__ == '__main__':
    for i in xrange(20):
        print isUgly(i), i

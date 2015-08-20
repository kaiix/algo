#  https://leetcode.com/problems/add-digits/

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    result = num
    while result >= 10:
        result = reduce(lambda x,y: x+y, map(int, str(result)))
    return result

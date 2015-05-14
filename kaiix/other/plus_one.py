#  https://leetcode.com/problems/plus-one/


def plusOne(digits):
    carry = 1
    length = len(digits)
    for i in xrange(length):
        d = digits[length-i-1] + carry
        carry = d / 10
        digits[length-i-1] = d % 10
    if carry:
        digits.insert(0, carry)
    return digits


if __name__ == '__main__':
    print plusOne([1])
    print plusOne([1, 3, 9])
    print plusOne([0])

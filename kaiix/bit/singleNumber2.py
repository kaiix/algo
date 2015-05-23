#  https://leetcode.com/problems/single-number-ii/


def singleNumber(nums):
    count = [0] * 32
    for digit in nums:
        idx = 0
        digit &= 0xffffffff
        while digit:
            count[idx] += digit & 1
            idx += 1
            digit = digit >> 1
    result = 0
    for i in xrange(len(count)):
        b = count[i] % 3
        if b:
            result |= b << i
    result = result & 0xffffffff
    return -(result & 0x80000000) + (result & 0x7fffffff)


if __name__ == '__main__':
    print singleNumber([-2, 2, -2, -2])
    print singleNumber([-2, -1, -2, -2])

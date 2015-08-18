#  https://leetcode.com/problems/reverse-bits/


def reverseBits(n):
    result = 0
    for i in xrange(32):
        b = (n >> i) & 1
        if b == 0:
            continue
        result |= b << (32-i-1)
    return result


if __name__ == '__main__':
    print reverseBits(43261596)

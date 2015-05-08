#  https://leetcode.com/problems/number-of-1-bits/


def hammingWeight(n):
    count = 0
    while n:
        count += (n & 1)
        n = n >> 1
    return count


if __name__ == '__main__':
    print hammingWeight(11)

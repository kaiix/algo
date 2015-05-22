#  https://leetcode.com/problems/rotate-array/


def rotate(nums, k):
    for i in xrange(k):
        last = nums.pop()
        nums.insert(0, last)


if __name__ == '__main__':
    n = range(1, 8)
    rotate(n, 3)
    print n

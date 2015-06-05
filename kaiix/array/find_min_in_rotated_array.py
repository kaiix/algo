#  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def findMin(nums):
    if len(nums) <= 0:
        return -1

    prev = nums[0]
    i = 1
    while (i < len(nums) and prev < nums[i]):
        i += 1
    if i == len(nums):
        return nums[0]
    else:
        return nums[i]


if __name__ == '__main__':
    print findMin([3, 4, 5, 6, 0, 1, 2])

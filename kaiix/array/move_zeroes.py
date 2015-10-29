#  https://leetcode.com/problems/move-zeroes


def moveZeroes(nums):
    firstZeroIndex = 0
    length = len(nums)
    while True:
        while firstZeroIndex < length and nums[firstZeroIndex] != 0:
            firstZeroIndex += 1
        nonZeroIndex = firstZeroIndex + 1
        while nonZeroIndex < length and nums[nonZeroIndex] == 0:
            nonZeroIndex += 1
        if nonZeroIndex >= length:
            break
        nums[firstZeroIndex], nums[nonZeroIndex] = nums[nonZeroIndex], nums[firstZeroIndex]
        firstZeroIndex += 1

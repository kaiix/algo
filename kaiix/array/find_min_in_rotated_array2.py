#  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/


def findMin2(nums):
    if len(nums) <= 0:
        return -1

    prev, i = nums[0], 1
    while (i < len(nums)) and (nums[i] >= prev):
        i += 1

    return nums[0] if i == len(nums) else nums[i]


def findMin(nums):
    if len(nums) <= 0:
        return -1

    i, j = 0, len(nums)-1
    while i < j:
        mid = (i+j) / 2
        if nums[mid] >= nums[i] and nums[mid] < nums[j]:
            return nums[i]
        elif nums[mid] == nums[j]:
            j -= 1
        if nums[mid] < nums[i]:
            j = mid
        elif nums[mid] > nums[j]:
            i = mid + 1
    return nums[i]


if __name__ == '__main__':
    print findMin([3, 4, 5, 1, 2])
    print findMin([3, 3, 1, 2, 3])

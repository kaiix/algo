#  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def findMin(nums):
    if len(nums) <= 0:
        return -1

    i, j = 0, len(nums)-1
    while i < j:
        if nums[i] < nums[j]:
            return nums[i]
        mid = (i+j) / 2
        if nums[mid] >= nums[i]:
            i = mid + 1
        else:
            j = mid
    return nums[i]

def findMin2(nums):
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

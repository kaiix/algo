#  https://leetcode.com/problems/kth-largest-element-in-an-array/


def findKthLargest(nums, k):
    nums, pivot = pivoting(nums)
    if pivot+1 == k:
        return nums[pivot]
    elif pivot+1 < k:
        return findKthLargest(nums[pivot+1:], k-pivot-1)
    else:
        return findKthLargest(nums[:pivot], k)


#  pivot index = 0
def pivoting(nums):
    r, p, q = 0, 0, 1
    for q in xrange(1, len(nums)):
        if nums[q] > nums[r]:
            nums[p+1], nums[q] = nums[q], nums[p+1]
            p += 1
    nums[r], nums[p] = nums[p], nums[r]
    return nums, p


if __name__ == '__main__':
    print findKthLargest([3, 2, 1, 5, 6, 4],  2)

#  https://leetcode.com/problems/contains-duplicate-ii/


def containsNearbyDuplicate(nums, k):
    for i in xrange(len(nums)):
        for j in xrange(i+1, i+k+1):
            if j >= len(nums):
                break
            if nums[i] == nums[j]:
                return True
    return False


def containsNearbyDuplicate2(nums, k):
    indexing = {}
    for i in xrange(len(nums)):
        if nums[i] in indexing:
            if i - indexing[nums[i]] <= k:
                return True
        indexing[nums[i]] = i
    return False


if __name__ == '__main__':
    print containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3)

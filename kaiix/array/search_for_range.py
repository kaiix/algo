#  https://leetcode.com/problems/search-for-a-range/


def searchRange(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    if nums[0] == nums[-1]:
        if nums[0] == target:
            return [0, len(nums)-1]
        else:
            return [-1, -1]
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high) / 2
        if nums[mid] == target:
            s, e = mid-1, mid+1
            if nums[0] != target:
                while s >= 0:
                    if nums[s] < target:
                        break
                    s -= 1
                s += 1
            else:
                s = 0
            if nums[-1] != target:
                while e < len(nums):
                    if nums[e] > target:
                        break
                    e += 1
                e -= 1
            else:
                e = len(nums)-1
            return [s, e]
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return [-1, -1]

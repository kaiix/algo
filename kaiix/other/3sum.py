#  https://leetcode.com/problems/3sum/


def threeSum(nums):
    result = []
    nums = sorted(nums)
    processed = {}
    idx = 0
    while idx < len(nums):
        val = nums[idx]
        if val in processed or 0-val in processed:
            idx += 1
            continue
        complements = twoSum(nums, idx+1, 0-val)
        for c in complements:
            c.insert(0, val)
            item = tuple(c)
            if item not in result:
                result.append(item)
        processed[val], processed[0-val] = True,  True
        idx += 1
    return result


def twoSum(nums, start, target):
    result = []
    l, r = start, len(nums)-1
    while l < r:
        diff = target-nums[l]
        if diff == nums[r]:
            result.append([nums[l], nums[r]])
            l += 1
            r -= 1
        elif diff < nums[r]:
            r -= 1
        else:
            l += 1
    return result


if __name__ == '__main__':
    print threeSum([3, 0, -2, -1, 1, 2])

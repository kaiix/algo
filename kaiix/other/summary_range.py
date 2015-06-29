#  https://leetcode.com/problems/summary-ranges/


def summaryRanges(nums):
    if len(nums) <= 1:
        return map(str, nums)
    result = []
    i, j = 0, 1
    while i < len(nums):
        if (j >= len(nums)) or (nums[j] > nums[j-1]+1):
            if i < j-1:
                result.append('%s->%s' % (nums[i], nums[j-1]))
            else:
                result.append(str(nums[j-1]))
            i = j
        j += 1
    return result

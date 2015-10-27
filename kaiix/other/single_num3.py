#  https://leetcode.com/problems/single-number-iii/


def singleNumber(nums):
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
        else:
            result.remove(i)
    return result

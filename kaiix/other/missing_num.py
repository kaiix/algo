#  https://leetcode.com/problems/missing-number/


def missingNumber(nums):
    largest = sorted(nums)[-1]
    diff = set(range(largest+1))-set(nums)
    if diff:
        return diff.pop()
    else:
        return largest+1

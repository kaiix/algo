#  https://leetcode.com/problems/contains-duplicate/


def containsDuplicate(nums):
    return len(set(nums)) != len(nums)

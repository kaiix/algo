#  https://leetcode.com/problems/two-sum/


def twoSum(nums, target):
    complements = {}
    for i in xrange(len(nums)):
        c = target - nums[i]
        if nums[i] in complements:
            return (complements[nums[i]], i+1)
        else:
            complements[c] = i+1
    return None


if __name__ == '__main__':
    print twoSum([2, 7, 11, 15], 9)

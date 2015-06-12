#  https://leetcode.com/problems/subsets/


def subsets(nums):
    if not nums:
        return [[]]
    sets = subsets(nums[1:])
    result = sets[:]
    for s in sets:
        if len(s) == 0:
            result.append([nums[0]])
        else:
            i = 0
            while (i < len(s) and nums[0] > s[i]):
                i += 1
            subset = s[:]
            if i < len(s):
                subset.insert(i, nums[0])
            else:
                subset.append(nums[0])
            result.append(subset)
    return result


if __name__ == '__main__':
    print subsets([4, 0, 1])

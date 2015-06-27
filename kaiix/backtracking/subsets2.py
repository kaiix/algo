#  https://leetcode.com/problems/subsets-ii/


def subsets(nums):
    if not nums:
        return [()]
    sets = subsets(nums[1:])
    result = set(sets[:])
    for s in sets:
        if len(s) == 0:
            result.add((nums[0],))
        else:
            i = 0
            while (i < len(s) and nums[0] > s[i]):
                i += 1
            subset = list(s)
            if i < len(s):
                subset.insert(i, nums[0])
            else:
                subset.append(nums[0])
            result.add(tuple(subset))
    return list(result)


if __name__ == '__main__':
    print subsets([1, 2, 2])

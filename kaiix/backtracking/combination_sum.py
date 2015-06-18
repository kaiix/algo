#  https://leetcode.com/problems/combination-sum/


def combinationSum(candidates, target):
    return _combinationSum(sorted(candidates), target)


def _combinationSum(candidates, target):
    if target == 0:
        return [[]]
    elif not candidates:
        return []
    elif target < candidates[0]:
        return []
    elif target == candidates[0]:
        return [[target]]
    else:
        result = []
        for i in xrange(len(candidates)):
            times = 1
            while candidates[i]*times <= target:
                combinations = _combinationSum(candidates[i+1:], target-candidates[i]*times)
                for j in combinations:
                    result.append([candidates[i]]*times+j)
                times += 1
        return result


# slower
# sorted candidates
def cs(candidates, target):
    if len(candidates) <= 0 or target <= 0:
        return []

    result = cs(candidates[1:], target)

    if candidates[0] == target:
        result.append([candidates[0]])
    elif candidates[0] < target:
        solutions = cs(candidates, target-candidates[0])
        for s in solutions:
            result.append([candidates[0]] + s)

    return result


if __name__ == '__main__':
    print combinationSum([2, 3, 6, 7], 7)
    print combinationSum([1, 2], 3)
    print combinationSum([8, 7, 4, 3], 11)

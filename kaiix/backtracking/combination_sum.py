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


if __name__ == '__main__':
    print combinationSum([2, 3, 6, 7], 7)
    print combinationSum([1, 2], 3)
    print combinationSum([8, 7, 4, 3], 11)

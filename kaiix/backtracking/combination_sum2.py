#  https://leetcode.com/problems/combination-sum-ii/


def combinationSum2(candidates, target):
    if target == 0:
        return [[]]
    elif len(candidates) == 0:
        return []
    else:
        if candidates[0] < target:
            result = combinationSum2(candidates[1:], target)
            combinations = combinationSum2(candidates[1:], target-candidates[0])
            for c in combinations:
                pos = 0
                while pos < len(c) and c[pos] < candidates[0]:
                    pos += 1
                solution = list(c)
                solution.insert(pos, candidates[0])
                result.append(tuple(solution))
        elif candidates[0] == target:
            result = combinationSum2(candidates[1:], target)
            result.append((candidates[0],))
        else:
            result = combinationSum2(candidates[1:], target)
        return list(set(result))


if __name__ == '__main__':
    print combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

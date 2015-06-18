#  https://leetcode.com/problems/combination-sum-iii/


def combinationSum3(k, n):
    return combine(1, 9, k, n)


def combine(start, end, k, n):
    if start > end:
        return []
    if k <= 0:
        return []
    if n <= 0:
        return []
    if k == 1 and n == start:
        return [[start]]

    result = []
    combinations = combine(start+1, end, k, n)
    result.extend(combinations)
    combinations = combine(start+1, end, k-1, n-start)
    for c in combinations:
        result.append([start]+c)
    return result


if __name__ == '__main__':
    print combinationSum3(2, 5)

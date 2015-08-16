#  https://leetcode.com/problems/longest-consecutive-sequence/


def longestConsecutive(nums):
    if not nums:
        return 0

    lower, upper = {}, {}  # saved lower bounds and upper bounds
    for i in nums:
        if i in lower:
            l, u = lower.pop(i)
            lower[i-1] = (i, u)
            upper[u+1] = (i, u)
        elif i in upper:
            l, u = upper.pop(i)
            upper[i+1] = (l, i)
            lower[l-1] = (l, i)
        elif i in lower and i in upper:
            l, _ = upper.pop(i)
            _, u = lower.pop(i)
            lower[l-1] = (l, u)
            upper[u+1] = (l, u)
        else:
            lower[i-1] = (i, i)
            upper[i+1] = (i, i)
        print lower, upper
    return max(map(lambda r: r[1]-r[0]+1, lower.values()))


if __name__ == '__main__':
    print longestConsecutive([-1, 1, 0])

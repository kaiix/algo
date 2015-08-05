#  https://leetcode.com/problems/product-of-array-except-self/


def productExceptSelf(nums):
    n = len(nums)
    forward, backward = [0] * n, [0] * n
    for i in xrange(n):
        if i > 0:
            forward[i] = nums[i] * forward[i-1]
            backward[n-i-1] = nums[n-i-1] * backward[n-i]
        else:
            forward[i] = nums[i]
            backward[n-i-1] = nums[n-i-1]
    result = []
    for i in xrange(n):
        before = forward[i-1] if i > 0 else 1
        after = backward[i+1] if i < n-1 else 1
        result.append(before*after)
    return result

#  https://leetcode.com/problems/maximum-product-subarray/


def maxProduct(nums):
    if len(nums) == 1:
        return nums[0]

    dp = [[0, 0] for i in xrange(len(nums))]  # reduce space cost
    dp[0][0] = max(nums[0], 0)
    dp[0][1] = min(nums[0], 0)
    for i in xrange(1, len(nums)):
        p = [nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1]]
        dp[i][0] = max(max(p), 0)  # maximum positive
        dp[i][1] = min(min(p), 0)  # minimum negetive
    import itertools
    return max(itertools.chain(*dp))


if __name__ == '__main__':
    print maxProduct([-2])
    print maxProduct([-2, 3, -4])
    print maxProduct([-2, 0, -2, -2])

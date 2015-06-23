#  https://leetcode.com/problems/house-robber/


def rob(nums):
    if not nums:
        return 0

    dp = [0] * len(nums)
    for i in xrange(len(nums)):
        if i < 1:
            dp[i] = nums[i]
        elif i < 2:
            dp[i] = max(nums[i], dp[i-1])
        else:
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
    return dp[-1]


if __name__ == '__main__':
    print rob([3, 8, 10, 20, 50, 60, 39, 20, 10])
    print rob([1, 2, 3, 4, 5])
    print rob([1, 8, 4])

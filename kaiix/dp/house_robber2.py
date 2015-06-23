#  https://leetcode.com/problems/house-robber-ii/


def rob(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[1:]), rob(nums[:-1]))


def _rob(nums):
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
    print rob([8, 6, 7, 3, 10, 20, 1, 20])
    print rob([8, 6, 10, 1])
    print rob([8, 6, 10])

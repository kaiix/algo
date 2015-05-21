#  https://leetcode.com/problems/house-robber/


def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0] + rob(nums[2:]), rob(nums[1:]))


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    memoize = None

    def rob(self, nums):
        self.memoize = {}
        return self._rob(nums, 0)

    def _rob(self, nums, pos):
        if pos >= len(nums):
            return 0
        else:
            if self.memoize.get(pos+1) is None:
                self.memoize[pos+1] = self._rob(nums, pos+1)
            if self.memoize.get(pos+2) is None:
                self.memoize[pos+2] = self._rob(nums, pos+2)
            return max(nums[pos] + self.memoize[pos+2], self.memoize[pos+1])


if __name__ == '__main__':
    print rob([3, 8, 10, 20, 50, 60, 39, 20, 10])
    print rob([1, 2, 3, 4, 5])
    print rob([1, 8, 4])

    print Solution().rob([3, 8, 10, 20, 50, 60, 39, 20, 10])
    print Solution().rob([1, 2, 3, 4, 5])
    print Solution().rob([1, 8, 4])

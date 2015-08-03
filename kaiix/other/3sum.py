#  https://leetcode.com/problems/3sum/


def threeSum(nums):
    nums = sorted(nums)
    result = []
    i = 0
    for i in xrange(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        diff = 0-nums[i]
        while l < r:
            if nums[l] + nums[r] == diff:
                result.append((nums[i], nums[l], nums[r]))
                while l < r:
                    l += 1
                    if l < r and nums[l] != nums[l-1]:
                        break
                while r > l:
                    r -= 1
                    if r > l and nums[r] != nums[r+1]:
                        break
            elif nums[l] + nums[r] < diff:
                l += 1
            else:
                r -= 1
    return result


if __name__ == '__main__':
    print threeSum([3, 0, -2, -1, 1, 2])

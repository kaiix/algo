#  https://leetcode.com/problems/4sum/


def fourSum(nums, target):
    nums = sorted(nums)
    result = []

    for i in xrange(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        s = target - nums[i]
        for j in xrange(i+1, len(nums)):
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            l, r = j+1, len(nums)-1
            while l < r:
                if nums[j]+nums[l]+nums[r] == s:
                    result.append((nums[i], nums[j], nums[l], nums[r]))
                    while l < r:
                        l += 1
                        if l < r and nums[l] != nums[l-1]:
                            break
                    while l < r:
                        r -= 1
                        if r > l and nums[r] != nums[r+1]:
                            break
                elif nums[j]+nums[l]+nums[r] < s:
                    l += 1
                else:
                    r -= 1
    return result


if __name__ == '__main__':
    print fourSum([0, 1, 2, -1, 0, -1, 3, 0, 0, 0], 1)

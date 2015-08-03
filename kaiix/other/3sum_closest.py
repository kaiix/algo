#  https://leetcode.com/problems/3sum-closest/


def threeSumClosest(nums, target):
    nums = sorted(nums)
    closest = None
    for i in xrange(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i]+nums[l]+nums[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            if s == target:
                closest = target
                break
            elif closest is None or abs(target-s) < abs(target-closest):
                closest = s
    return closest


if __name__ == '__main__':
    print threeSumClosest([-1, 2, 1, -4], 1)

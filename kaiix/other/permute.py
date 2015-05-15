#  https://leetcode.com/problems/permutations/


def permute(nums):
        if len(nums) <= 1:
            return [nums]

        result = []
        for i in xrange(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            for s in permute(nums[1:]):
                s.insert(0, nums[0])
                result.append(s)
        return result


if __name__ == '__main__':
    print permute([1, 2, 3])


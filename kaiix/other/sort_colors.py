#  https://leetcode.com/problems/sort-colors/


def sortColors(nums):
    counter = [0] * 3
    for i in nums:
        counter[i] += 1
    idx = 0
    for color in range(3):
        for _ in xrange(counter[color]):
            nums[idx] = color
            idx += 1


if __name__ == '__main__':
    print sortColors([0, 1, 0, 2, 0, 1, 0])

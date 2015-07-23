#  https://leetcode.com/problems/container-with-most-water/

#  Devise a plan (when you stuck)
#  - Keep the unknown in mind
#  - What are the conditions, notice those implied conditions (e.g.
#  sorted/unsored array)
#  - Transform a condition, make it special and try to solve the problem


def maxArea(height):
    i, j = 0, len(height)-1
    result = 0
    while i < j:
        if height[i] < height[j]:
            result = max(height[i] * (j-i), result)
            i += 1
        else:
            result = max(height[j] * (j-i), result)
            j -= 1
    return result


if __name__ == '__main__':
    print maxArea([2, 4, 3, 1])

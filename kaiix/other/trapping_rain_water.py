#  https://leetcode.com/problems/trapping-rain-water/


def trap(height):
    s, i, bars = 0, 0, []
    while i < len(height):
        if bars and height[i] >= bars[-1]:
            if bars[0] <= height[i]:
                h = bars[0]
                while bars:
                    s += h - bars.pop()
            else:
                j = len(bars)-1
                while j >= 0 and bars[j] < height[i]:
                    s += height[i] - bars[j]
                    bars[j] = height[i]
                    j -= 1
        bars.append(height[i])
        i += 1
    return s


if __name__ == '__main__':
    print trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

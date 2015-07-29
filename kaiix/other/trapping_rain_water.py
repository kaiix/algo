#  https://leetcode.com/problems/trapping-rain-water/


def trap(height):
    if len(height) <= 1:
        return 0

    stk = []
    i = 0
    s = 0
    while i < len(height):
        if stk and height[i] > height[stk[-1][1]]:
            h = min(height[stk[0][1]], height[i])
            w = 0
            while stk and height[stk[-1][1]] <= height[i]:
                bar = stk.pop()
                w += bar[0]
                s += (h - height[bar[1]]) * bar[0]
            if h == height[i]:
                stk.append((w+1, i))
            else:
                stk.append((1, i))
        else:
            stk.append((1, i))
        i += 1
    return s


if __name__ == '__main__':
    print trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

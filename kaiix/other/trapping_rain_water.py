#  https://leetcode.com/problems/trapping-rain-water/


def trap(height):
    if len(height) <= 1:
        return 0

    stk = []
    i = 0
    s = 0
    while i < len(height):
        if not stk:
            stk.append((1, height[i]))
            i += 1
        elif height[i] <= stk[-1][1]:
            stk.append((1, height[i]))
            i += 1
        else:
            aux = []
            while stk and stk[-1][1] <= height[i]:
                aux.append(stk.pop())
            if stk:
                lhs = stk[-1]
            else:
                lhs = aux.pop()
            h = min(lhs[1], height[i])
            w = 0
            for bar in aux:
                w += bar[0]
                s += (h - bar[1]) * bar[0]
            if lhs[1] < height[i]:
                stk.append((1, height[i]))
            else:
                stk.append((w+1, height[i]))
            i += 1
    return s


if __name__ == '__main__':
    print trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

#  https://leetcode.com/problems/distinct-subsequences/


def numDistinct2(s, t):
    if not t:
        return 1
    elif not s:
        return 0
    else:
        if s[0] != t[0]:
            return numDistinct2(s[1:], t)
        else:
            return numDistinct2(s[1:], t[1:]) + numDistinct2(s[1:], t)


def numDistinct(s, t):
    if len(s) == 0 and len(t) == 0:
        return 1
    if len(s) == 0 and len(t) > 0:
        return 0
    if len(s) > 0 and len(t) == 0:
        return 1
    if len(s) < len(t):
        return 0

    dp = [[0] * len(t) for i in xrange(len(s))]
    for i in reversed(xrange(len(s))):
        for j in reversed(xrange(len(t))):
            if len(t)-j > len(s)-i:
                break
            if s[i] != t[j]:
                if i+1 >= len(s):
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j]
                subnum = 0
            else:
                if j+1 >= len(t):
                    subnum = 1
                elif i+1 >= len(s):
                    subnum = 0
                else:
                    subnum = dp[i+1][j+1]
            if i+1 < len(s):
                dp[i][j] = dp[i+1][j] + subnum
            else:
                dp[i][j] = subnum
    return dp[0][0]


if __name__ == '__main__':
    print numDistinct('b', 'a')
    print numDistinct('rabbbit', 'rabbit')

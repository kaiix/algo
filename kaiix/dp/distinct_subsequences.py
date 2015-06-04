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
    dp = [[0] * (len(t)+1) for i in xrange(len(s)+1)]
    for i in xrange(len(s)+1):
        dp[i][len(t)] = 1

    for i in reversed(xrange(len(s))):
        for j in reversed(xrange(len(t))):
            if len(t)-j > len(s)-i:
                break
            if s[i] != t[j]:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
    return dp[0][0]


if __name__ == '__main__':
    print numDistinct('b', 'a')
    print numDistinct('rabbbit', 'rabbit')

#  https://leetcode.com/problems/decode-ways://leetcode.com/problems/decode-ways/

mapping = map(str, xrange(1, 26))


def can_decode(code):
    return code in mapping


def numDecodings(s):
    dp = [0] * len(s)
    for i in xrange(len(s)):
        if can_decode(s[i]):
            if i-1 >= 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = 1
        if (0 < i < len(s)) and can_decode(s[i-1:i+1]):
            if i-2 >= 0:
                dp[i] += dp[i-2]
            else:
                dp[i] += 1
    return dp[-1]


if __name__ == '__main__':
    print numDecodings('12')

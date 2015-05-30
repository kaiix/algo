#  https://leetcode.com/problems/word-break/


def wordBreak(s, wordDict):
    if len(s) == 0:
        return len(wordDict) == 0

    dp = [False] * len(s)

    for i in xrange(len(s)):
        substr = s[:i+1]
        if substr in wordDict:
            dp[i] = True
            continue
        for j in reversed(xrange(i)):
            if dp[j]:
                substr = s[j+1:i+1]
            if substr in wordDict:
                dp[i] = True
                break

    return dp[-1]

if __name__ == '__main__':
    print wordBreak('leetcode', ['leet', 'code'])
    print wordBreak('goodboy', ['g', 'oo', 'd', 'boy'])
    print wordBreak('a', ['a'])

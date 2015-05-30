#  https://leetcode.com/problems/word-break/


def wordBreak(s, wordDict):
    if len(s) == 0:
        return len(wordDict) == 0

    dp = [False] * len(s)
    for i in xrange(len(s)):
        if i == 0:
            for w in wordDict:
                if w == s[0]:
                    dp[0] = True
                    break
        else:
            for j in reversed(xrange(i)):
                if dp[j]:
                    substr = s[j+1:i+1]
                else:
                    substr = s[:i+1]
                for w in wordDict:
                    if substr == w:
                        dp[i] = True
                        break
                if dp[i]:
                    break
    return dp[-1]


if __name__ == '__main__':
    print wordBreak('leetcode', ['leet', 'code'])
    print wordBreak('goodboy', ['g', 'oo', 'd', 'boy'])
    print wordBreak('a', ['a'])

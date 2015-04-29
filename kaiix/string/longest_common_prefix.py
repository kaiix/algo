#  https://leetcode.com/problems/longest-common-prefix/


def longestCommonPrefix(strs):
    if not strs:
        return ''

    idx = 0
    while True:
        ch = None
        for s in strs:
            if idx >= len(s):
                return s[:idx]
            if not ch:
                ch = s[idx]
                continue
            if s[idx] != ch:
                return s[:idx]
        idx += 1
    return ''


if __name__ == '__main__':
    print longestCommonPrefix([])
    print longestCommonPrefix(['abc'])
    print longestCommonPrefix(['a', 'ab'])
    print longestCommonPrefix(['a', 'ab', 'c'])
    print longestCommonPrefix(['ababa', 'aba', 'ab'])

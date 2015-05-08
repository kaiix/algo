#  https://leetcode.com/problems/implement-strstr/


def strStr(haystack, needle):
    if len(needle) == 0:
        return 0

    for i in xrange(len(haystack)):
        if len(needle) > len(haystack)-i:
            return -1

        for j in xrange(len(needle)):
            if needle[j] != haystack[i+j]:
                break

        if j == len(needle)-1 and needle[j] == haystack[i+j]:
            return i

    return -1


if __name__ == '__main__':
    print strStr('this is a simple string', 'simple')
    print strStr('foo', '')
    print strStr('foo bar', 'o b')
    print strStr('aaa', 'aaaa')
    print strStr('', '')
    print strStr('mississippi', 'pi')

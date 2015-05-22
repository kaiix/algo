#  https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s, t):
        from itertools import izip
        cmap = {}
        for x, y in izip(s, t):
            if not cmap.get(x):
                if y in cmap.itervalues():  # two key cannot map to a same value
                    return False
                else:
                    cmap[x] = y
            elif cmap[x] != y:
                return False
        return True


if __name__ == '__main__':
    print Solution().isIsomorphic('foo', 'foo')
    print Solution().isIsomorphic('foo', 'bar')
    print Solution().isIsomorphic('ab', 'aa')

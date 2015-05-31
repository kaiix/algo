#  https://leetcode.com/problems/edit-distance/


class Solution:
    cache = {}

    def minDistance(self, word1, word2):
        self.cache = {}
        return self._minDistance(word1, word2, 0, 0)

    def _minDistance(self, word1, word2, i, j):
        if self.cache.get((i, j)):
            return self.cache[(i, j)]

        if i >= len(word1):
            return max(len(word2)-j, 0)
        if j >= len(word2):
            return max(len(word1)-i, 0)

        if word1[i] == word2[j]:
            self.cache[(i, j)] = self._minDistance(word1, word2, i+1, j+1)
        else:
            self.cache[(i, j)] = 1 + min(
                self._minDistance(word1, word2, i, j+1),  # insert
                self._minDistance(word1, word2, i+1, j),  # delete
                self._minDistance(word1, word2, i+1, j+1),  # replace
            )
        return self.cache[(i, j)]


def minDistance2(word1, word2):
    if len(word1) <= 0:
        return len(word2)
    if len(word2) <= 0:
        return len(word1)

    if word1[0] == word2[0]:
        return minDistance2(word1[1:], word2[1:])
    else:
        return 1 + min(
            minDistance2(word1, word2[1:]),  # insert
            minDistance2(word1[1:], word2),  # delete
            minDistance2(word1[1:], word2[1:]),  # replace
        )


if __name__ == '__main__':
    print Solution().minDistance('c', '')
    print Solution().minDistance('', 'c')
    print Solution().minDistance('arc', 'rc')
    print Solution().minDistance('football', 'foobar')

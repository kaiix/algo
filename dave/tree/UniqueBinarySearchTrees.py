class Solution:
    # @return an integer
    def numTrees(self, n):
        """Catalan number"""
        result = [1]
        for i in range(1, n + 1):
            number = 0
            for j in range((i + 1) / 2):
                tmp = result[i - j - 1] * result[j]
                if i - j - 1 > j:
                    tmp *= 2
                number += tmp
            result.append(number)
        return result[n]

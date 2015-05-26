#  https://leetcode.com/problems/unique-paths-ii/


def uniquePathsWithObstacles2(obstacleGrid):
        dp = []
        for i in xrange(len(obstacleGrid)):
            row = []
            for j in xrange(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    row.append(0)
                else:
                    if i == 0 and j == 0:
                        # assume first one not obstacled
                        row.append(1)
                    elif i == 0:
                        row.append(row[j-1])
                    elif j == 0:
                        row.append(dp[i-1][j])
                    else:
                        row.append(row[j-1] + dp[i-1][j])
            dp.append(row)
        return dp[-1][-1]


# slower than previous, but easier for reading
def uniquePathsWithObstacles(obstacleGrid):
        dp = [[0] * len(obstacleGrid[0])] * len(obstacleGrid)
        for i in xrange(len(obstacleGrid)):
            for j in xrange(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        # assume first one not obstacled
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    print uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

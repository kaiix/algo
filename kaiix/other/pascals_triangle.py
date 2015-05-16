#  https://leetcode.com/problems/pascals-triangle/


def generate(numRows):
    result = []
    for i in xrange(numRows):
        row = []
        for j in xrange(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i-1][j-1]+result[i-1][j])
        result.append(row)
    return result


if __name__ == '__main__':
    print generate(5)

#  https://leetcode.com/problems/pascals-triangle-ii/


def getRow(rowIndex):
    lastRow = []
    for i in xrange(rowIndex+1):
        row = []
        for j in xrange(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(lastRow[j-1]+lastRow[j])
        lastRow = row
    return lastRow


if __name__ == '__main__':
    for i in xrange(5):
        print getRow(i)

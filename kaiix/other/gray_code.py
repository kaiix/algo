#  https://leetcode.com/problems/gray-code/


def grayCode(n):
    result = [0]
    for i in xrange(n):
        reflected = []
        msb = 1 << i
        for j in reversed(result):
            reflected.append(j | msb)
        result.extend(reflected)
    return result

#  http://en.wikipedia.org/wiki/Gray_code
#  Gray code, aka "reflected binary code"

if __name__ == '__main__':
    print grayCode(2)

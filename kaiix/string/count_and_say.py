# https://leetcode.com/problems/count-and-say/


def countAndSay(n):
    if n == 1:
        return '1'
    else:
        n -= 1
        said = '1'
        while True:
            if n == 0:
                break
            count, ch, result = 0, '', ''
            transformed = said + '$'  # use `$` as sentinel
            for i in transformed:
                if i != ch:
                    if count > 0:
                        result += "%d%s" % (count, ch)
                    ch = i
                    count = 0
                count += 1
            said = result
            n -= 1
        return said


if __name__ == '__main__':
    for n in range(1, 10):
        print countAndSay(n)

# https://oj.leetcode.com/problems/integer-to-roman/

ROMANS = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}


def itor(n):
    def _roman(x, pos):
        ones = ROMANS[10**pos]
        if pos < 3:
            fives = ROMANS[10**pos * 5]
            tens = ROMANS[10**pos * 10]

        if x % 5 == 4:
            if x / 5:
                return ones + tens
            else:
                return ones + fives
        elif x < 5:
            return ones * x
        else:
            return fives + ones * (x-5)

    result = [_roman(int(x), pos) for pos, x in enumerate(reversed(str(n)))]
    return ''.join(reversed(result))

print itor(1954)
print itor(1990)
print itor(2014)

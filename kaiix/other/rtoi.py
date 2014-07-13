# https://oj.leetcode.com/problems/roman-to-integer/

ROMANS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def romansToInt(s):
    nums = map(lambda c: ROMANS[c], s)

    result = 0
    prev = 0
    num = 0
    for num in nums:
        if num > prev:
            result -= prev
        else:
            result += prev
        prev = num
    result += num
    return result

print romansToInt('XXII')
print romansToInt('VI')
print romansToInt('IV')
print romansToInt('MCMIV')
print romansToInt('MCMLIV')
print romansToInt('MCMXC')
print romansToInt('I')
print romansToInt('')

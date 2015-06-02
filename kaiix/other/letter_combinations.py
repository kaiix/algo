#  https://leetcode.com/problems/letter-combinations-of-a-phone-number/

mapping = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def letterCombinations(digits):
    if not digits:
        return []
    elif len(digits) == 1:
        return list(mapping[digits[0]])
    else:
        result = []
        for c in mapping[digits[0]]:
            result.extend([c + s for s in letterCombinations(digits[1:])])
        return result


if __name__ == '__main__':
    print letterCombinations('2')
    print letterCombinations('23')

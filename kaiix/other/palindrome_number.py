#  https://leetcode.com/problems/palindrome-number/


def isPalindrome(x):
    if x < 0:
        return False
    if x >= 0 and x <= 9:
        return True

    length, y = 0, x
    while y > 9:
        y /= 10
        length += 1
    high, low = length, 0
    while high > low:
        msd = (x / 10**high) % 10
        lsd = (x / 10**low) % 10
        if msd == lsd:
            high -= 1
            low += 1
        else:
            return False
    return True


if __name__ == '__main__':
    print isPalindrome(121)
    print isPalindrome(1021)

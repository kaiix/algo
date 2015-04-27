#  https://leetcode.com/problems/valid-palindrome/


def isPalindrome(s):
    if not s:
        return True

    s = s.lower()
    i, j = 0, len(s)-1
    while i <= j:
        if s[i].isalnum() and s[j].isalnum() and s[i] == s[j]:
            i += 1
            j -= 1
        elif not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    print isPalindrome("race a car")
    print isPalindrome("A man, a plan, a canal: Panama")

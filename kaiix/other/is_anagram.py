#  https://leetcode.com/problems/valid-anagram/


def isAnagram(s, t):
    return sorted(s) == sorted(t)

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if not s:
            return ''
        return ' '.join(reversed(s.split()))

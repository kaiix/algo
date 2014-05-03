class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return " ".join(reversed([x for x in s.strip().split(' ') if len(x) > 0]))
        
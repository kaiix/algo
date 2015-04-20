class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if len(stack) == 0 or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return len(stack) == 0

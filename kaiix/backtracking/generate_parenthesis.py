#  https://leetcode.com/problems/generate-parentheses/


def generateParenthesis(n):
    pairs = [None] * (n+1)
    pairs[0] = []
    for i in xrange(1, n+1):
        if i == 1:
            pairs[i] = ["()"]
        else:
            parens = set()
            for j in xrange(1, i/2+1):
                for lhs in pairs[j]:
                    for rhs in pairs[i-j]:
                        parens.add(lhs+rhs)
                        parens.add(rhs+lhs)
                        if j == 1:
                            parens.add("("+rhs+")")
            pairs[i] = list(parens)
    return pairs[-1]


if __name__ == '__main__':
    print sorted(generateParenthesis(3))

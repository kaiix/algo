#  https://leetcode.com/problems/basic-calculator-ii/


def calculate(s):
    s = s.replace(' ', '')
    if len(s) <= 1:
        return int(s)
    s += '$'
    return _calculate(s, 0)


def nextOp(equation, begin):
    for i in xrange(begin, len(equation)):
        if not equation[i].isdigit():
            return i
    return -1


import operator

Op = {
    '+': operator.__add__,
    '-': operator.__sub__,
    '*': operator.__mul__,
    '/': operator.__truediv__,
}


def _calculate(equation, b):
    if b >= len(equation):
        return 0

    stk = []
    e = 0
    sign = 1
    while b <= len(equation):
        if equation[b] in '+-':
            sign = Op[equation[b]](0, 1)
            b += 1
        lhs = None
        while b <= len(equation):
            e = nextOp(equation, b)

            if lhs is None:
                lhs = sign * int(equation[b:e])

            if equation[e] == '$':
                break

            if e < 0 or equation[e] in '+-':
                break

            print lhs
            ahead = nextOp(equation, e+1)
            rhs = int(equation[e+1:ahead])
            print rhs
            print equation[e]
            lhs = int(Op[equation[e]](lhs, rhs))
            print lhs
            b = e + 1

        if equation[e] in '+-':
            stk.append(lhs)
            b = e
        else:
            stk.append(lhs)
            return sum(stk)


if __name__ == '__main__':
#    print calculate("3*2-5")
#    print calculate("3+2*2")
#    print calculate(" 3/2 ")
#    print calculate(" 3+5 / 2 ")
#    print calculate("7+8*2-2*0+10-16+7*0")
#    print calculate("8*8-8*8")
#    print calculate("2*3-3+2*3")
#    print calculate("0-37")
#    print calculate("37")
    print calculate("14-3/2")

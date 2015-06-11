#  https://leetcode.com/problems/combinations/


def combine(n, k):
    return select(1, n+1, k)


def select(start, end, num):
    if num == 1:
        return [[i] for i in xrange(start, end)]
    result = []
    for i in xrange(start, end):
        combinations = select(i+1, end, num-1)
        combinations = [[i]+c for c in combinations]
        result.extend(combinations)
    return result

if __name__ == '__main__':
    print combine(4, 2)

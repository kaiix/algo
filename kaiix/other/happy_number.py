#  https://leetcode.com/problems/happy-number/


def is_happy(n):
    cache = {}
    while True:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n /= 10
        n = sum(map(lambda x: x*x, digits))
        if n == 1:
            return True
        elif cache.get(n, False):
            return False
        else:
            cache[n] = True


if __name__ == '__main__':
    print is_happy(19)
    print is_happy(18)

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A:
            return -1
        elif A[0] == target:
            return 0
        elif len(A) == 1:
            return  -1

        r = self.findRight(A, 1, len(A) - 1)
        if A[0] == target:
            return 0
        elif A[0] < target:
            return self.bsearch(A, target, 1, r - 1)
        else:
            return self.bsearch(A, target, r, len(A) - 1)

    def findRight(self, A, b, e):
        if b >= e:
            if A[b] < A[0]:
                return b
            else:
                return b + 1
        m = (b + e) / 2
        if A[m] < A[0]:
            return self.findRight(A, b, m - 1)
        else:
            return self.findRight(A, m + 1, e)

    def bsearch(self, A, target, b, e):
        if b > e:
            return -1
        elif b == e:
            if A[b] == target:
                return b
            else:
                return -1
        m = (b + e) / 2
        if A[m] == target:
            return m
        elif A[m] < target:
            return self.bsearch(A, target, m + 1, e)
        else:
            return self.bsearch(A, target, b, m - 1)

    def search_bruteforce(self, A, target):
        if not A:
            return -1
        for i in range(len(A)):
            if A[i] == target:
                return i
        return -1


def main():
    sol = Solution()

    test_cases = [
        [[], 0],
        [[0], 0],
        [[-1], 0],
        [[-3, -1], 0],
        [[-1, 1], 0],
        [[4, 5, 6, 7, 0, 1, 2], 0],
        [[4, 5, 6, 7, 0, 1, 2], 1],
        [[4, 5, 6, 7, 0, 1, 2], 3],
        [[4, 5, 6, 7, 0, 1, 2], 4],
        [[4, 5, 6, 7, 0, 1, 2], 5],
        [[-2, -1, 0, 1, 2, 3, 4, -5, -3], 0],
    ]
    for test_case in test_cases:
        import time
        a = time.time()
        ret = sol.search(*test_case)
        b = time.time()
        print b - a, ret, test_case
        a = time.time()
        ret = sol.search_bruteforce(*test_case)
        b = time.time()
        print b - a, ret, test_case

if __name__ == "__main__":
    main()

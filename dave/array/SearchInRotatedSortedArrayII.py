class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a boolean
    def search(self, A, target):
        if not A:
            return False
        elif A[0] == target:
            return True
        elif len(A) == 1:
            return False

        r = self.findRight(A, 0, len(A) - 1)
        if A[0] == target:
            return True
        elif A[0] < target:
            return self.bsearch(A, target, 1, r - 1) != -1
        else:
            return self.bsearch(A, target, r, len(A) - 1) != -1

    def findRight(self, A, b, e):
        if b > e:
            return b
        elif b == e:
            return b + 1
        while b < e:
            if A[b] > A[b + 1]:
                return b + 1
            b += 1
        return b + 1

    def bsearch(self, A, target, b, e):
        if b > e:
            return -1
        elif A[b] == target:
            i = b - 1
            while i >= 0 and A[i] == target:
                i -= 1
            return i + 1
        elif b == e:
            return -1
        m = (b + e) / 2
        if A[m] == target:
            i = m - 1
            while i >= 0 and A[i] == target:
                i -= 1
            return i + 1
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
        [[-3, -3], 0],
        [[-1, 1, -1], 0],
        [[1, 1, 3], 3],
        [[-1, 1, -1, -1], 0],
        [[2, 2, 2, 0, 2, 2], 0],
        [[1, 2, 2, 2, 0, 1, 1], 0],
        [[1, 1, 1, 3, 1], 3],
        [[4, 5, 6, 7, 7, 0, 0, 1, 2], 0],
        [[4, 5, 6, 7, 7, 0, 1, 1, 2], 1],
        [[4, 5, 6, 7, 7, 0, 1, 2], 3],
        [[4, 5, 6, 7, 0, 1, 2], 4],
        [[4, 5, 5, 6, 7, 0, 1, 1, 2], 5],
        [[-2, -1, -1, 0, 0, 1, 2, 3, 4, -5, -3], 0],
        [[-2, -1, -1, 0, 0, 1, 2, 3, 4, -5, -5, -3], 0],
        [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 2],
    ]
    for test_case in test_cases:
        import time
        a = time.time()
        ret = sol.search(*test_case)
        b = time.time()
        print b - a, ret #, test_case
        a = time.time()
        ret = sol.search_bruteforce(*test_case)
        b = time.time()
        print b - a, ret #, test_case

if __name__ == "__main__":
    main()

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if not A:
            if not B:
                return 0
            M = len(B)
            if M % 2 == 1:
                return B[M / 2]
            return self.median2(B[M / 2 - 1], B[M / 2])

        N = len(A)
        if not B:
            if N % 2 == 1:
                return A[N / 2]
            return self.median2(A[N / 2 - 1], A[N / 2])

        M = len(B)
        if N > M:
           return self.findMedianUtil(B, 0, M, A, 0, N)
        return self.findMedianUtil(A, 0, N, B, 0, M)

    def median2(self, a, b):
        return (a + b) / 2.0

    def median3(self, a, b, c):
        # print 'median3', a, b, c
        return a + b + c - max(a, b, c) - min(a, b, c)

    def median4(self, a, b, c, d):
        # print 'median4', a, b, c, d
        return (a + b + c + d - max(a, b, c, d) - min(a, b, c, d)) / 2.0

    # http://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
    # This function assumes that N is smaller than or equal to M
    def findMedianUtil(self, A, start_idx_a, N, B, start_idx_b, M):
        # print start_idx_a, N, A
        # print start_idx_b, M, B
        # If the smaller array has two elements
        if N == 1:
            # Case 1: Both has 1 element, simply call median2()
            if M == 1:
                return self.median2(A[start_idx_a], B[start_idx_b])

            # Case 2: If the larger array has odd number of elements, then
            # consider the middle 3 elements of larger array and the only
            # element of smaller array. Take few examples like following
            # A = [9], B = [5, 8, 10, 20, 30] and
            # A = [1], B = [5, 8, 10, 20, 30]
            if M % 2 == 1:
                return self.median2(B[start_idx_b + M / 2],
                                    self.median3(A[start_idx_a],
                                                 B[start_idx_b + M / 2 - 1],
                                                 B[start_idx_b + M / 2 + 1]))

            # Case 3: If the larger array has even number of element, then
            # median will be one of the following 3 elements
            # 1) The middle two elements of larger array
            # 2) The only element of smaller array
            return self.median3(B[start_idx_b + M / 2],
                                B[start_idx_b + M / 2 - 1],
                                A[0])

        # If the smaller array has two elements
        elif N == 2:
            # Case 4: Both has 2 elements, simply call median4()
            if M == 2:
                return self.median4(A[start_idx_a], A[start_idx_a + 1],
                                    B[start_idx_b], B[start_idx_b + 1])

            # Case 5: If the larger array has odd number of elements, then
            # median will be one of the following 3 elements
            # 1) Middle element of larger array
            # 2) Max of first element of smaller array and element just
            #    before the middle in bigger array
            # 3) Min of second element of smaller array and element just
            #    after the middle in bigger array
            if M % 2 == 1:
                return self.median3(B[start_idx_b + M / 2],
                                    max(A[start_idx_a],
                                        B[start_idx_b + M / 2 - 1]),
                                    min(A[start_idx_a + 1],
                                        B[start_idx_b + M / 2 + 1]))

            # Case 6: If the larger array has even number of elements, then
            # median will be one of the following 4 elements
            # 1) & 2) The middle two elements of larger array
            # 3) Max of first element of smaller array and element
            #    just before the first middle element in bigger array
            # 4) Min of second element of smaller array and element
            #    just after the second middle in bigger array
            return self.median4(B[start_idx_b + M / 2],
                                B[start_idx_b + M / 2 - 1],
                                max(A[start_idx_a],
                                    B[start_idx_b + M / 2 - 2]),
                                min(A[start_idx_a + 1],
                                    B[start_idx_b + M / 2 + 1]))

        idx_a = (N - 1) / 2
        idx_b = (M - 1) / 2

        # If A[idx_a] <= B[idx_b], then median must exist in
        # A[idx_a....] and B[....len_b - idx_a]
        if A[start_idx_a + idx_a] <= B[start_idx_b + idx_b]:
            return self.findMedianUtil(A, start_idx_a + idx_a, N / 2 + 1,
                                       B, start_idx_b, M - idx_a)

        # if A[idx_a] > B[idx_b], then median must exist in
        # A[...idx_a] and B[idx_a....] */
        return self.findMedianUtil(A, start_idx_a, N / 2 + 1,
                                   B, start_idx_b + idx_a, M - idx_a)


def main():
    sol = Solution()

    test_cases = [
        [[], [1]],
        [[1], []],
        [[9], [5, 8, 10, 20, 30]],
        [[1], [5, 8, 10, 20, 30]],
        [[1, 2, 3], [4, 5, 6]],
        [[4, 5, 6], [1, 2, 3]],
        [[4, 5, 6], [1]],
        [[-1], [-3, -1]],
        [[-1, 1], [-2, 1, -3, 4, -1, 2, 1, -5, 4]],
        [[1, 1, 3, 3], [1, 1, 3, 3]],
        [[1, 3], [2, 4, 5, 6]],
        [[1, 2, 5], [3, 4, 6, 7]],
        [[1, 5, 6], [2, 3, 4, 7, 8]],
        [[1, 2, 6, 7], [3, 4, 5, 8]],
        [[1, 5, 6, 7], [2, 3, 4, 8, 9]],
    ]
    for test_case in test_cases:
        l1 = sorted(test_case[0])
        l2 = sorted(test_case[1])
        import time
        a = time.time()
        ret = sol.findMedianSortedArrays(l1, l2)
        b = time.time()
        print b - a, ret, l1, l2

if __name__ == "__main__":
    main()

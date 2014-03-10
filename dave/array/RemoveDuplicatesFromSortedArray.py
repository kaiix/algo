class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        last = -1
        i = 0
        while A and i < len(A):
            if last < 0 or A[last] != A[i]:
                last += 1
                A[last] = A[i]
            i += 1
        return last + 1

def main():
    sol = Solution()

    test_cases = [
        [1, 1, 2],
        [1, 1, 2, 3, 3],
        [1, 1, 1, 2, 2, 3],
    ]
    for test_case in test_cases:
        n = sol.removeDuplicates(test_case)
        print n, test_case

if __name__ == "__main__":
    main()

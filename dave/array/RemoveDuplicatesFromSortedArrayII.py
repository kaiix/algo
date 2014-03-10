class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        last = None
        count = 0
        i = 0
        while A and i < len(A):
            if last is None or last != A[i]:
                last = A[i]
                count = 1
            else:
                count += 1
                if count > 2:
                    A.pop(i)
                    i -= 1
            i += 1
        return len(A)

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

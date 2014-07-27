# https://oj.leetcode.com/problems/remove-element/


def removeElement(self, A, elem):
    """ removeElement([1, 2, 3, 1, 3, 2], 1) => 4, [2, 3, 3, 2]"""
    def swap(A, i, j):
        A[i], A[j] = A[j], A[i]

    def find_end(A, start, end, el):
        """ find new end which every element after that is *el* """
        while start <= end and A[end] == el:
            end -= 1
        return end

    def find_start(A, start, end, el):
        """ find new start which every element before that isn't *el* """
        while start <= end and A[start] != el:
            start += 1
        return start

    p = find_start(A, 0, len(A) - 1, elem)
    q = find_end(A, p, len(A) - 1, elem)
    while p < q:
        if A[p] == elem:
            swap(A, p, q)
            p = find_start(A, p+1, q, elem)
            q = find_end(A, p, q-1, elem)
    return q + 1


A = [1, 2, 3, 1, 3, 2]
n = removeElement(A, 1)
print A[:n]

A = [1, 2, 3, 1, 3, 2]
n = removeElement(A, 2)
print A[:n]

A = [1]
n = removeElement(A, 1)
print A[:n]

A = []
n = removeElement(A, 1)
print A[:n]

A = [2, 2, 3]
n = removeElement(A, 2)
print A[:n]

A = [0, 4, 4, 0, 4, 4, 4, 0, 2]
n = removeElement(A, 4)
print A[:n]

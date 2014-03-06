class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def deleteDuplicates(self, head, n):
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        i = 0
        node = head
        while i < length - n - 1:
            i += 1
            node = node.next
        if n == length:
            head = head.next
        elif node.next:
            node.next = node.next.next
        return head

def pprint(node):
    while node:
        print node.val,
        if node.next:
            print '->',
        node = node.next
    print ''

def main():
    sol = Solution()

    test_cases = [
        ([1, 1, 2], 2),
        ([1, 1, 2, 3, 3], 1),
        ([1, 2, 3, 4, 5], 2),
        ([1], 1),
    ]
    for test_case in test_cases:
        node = None
        last = None
        for i in range(len(test_case[0]), 0, -1):
            node = ListNode(test_case[0][i-1])
            node.next = last
            last = node
        node = sol.deleteDuplicates(node, test_case[1])
        pprint(node)

if __name__ == "__main__":
    main()

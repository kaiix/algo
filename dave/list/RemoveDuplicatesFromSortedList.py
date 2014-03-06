class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        current = head
        last = None
        while current:
            if not last:
                last = current
            elif current.val != last.val:
                last.next = current
                last = current
            current = current.next
            last.next = None
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
        [1, 1, 2],
        [1, 1, 2, 3, 3],
    ]
    for test_case in test_cases:
        node = None
        last = None
        for i in range(len(test_case), 0, -1):
            node = ListNode(test_case[i-1])
            node.next = last
            last = node
        node = sol.deleteDuplicates(node)
        pprint(node)

if __name__ == "__main__":
    main()

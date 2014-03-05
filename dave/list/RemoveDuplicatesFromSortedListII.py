class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        current = head
        new_head = None
        last = None
        test = None
        count = 0
        while current:
            if not test:
                test = current
                count = 1
            elif current.val != test.val:
                if count <= 1:
                    if last:
                        last.next = test
                    last = test
                    last.next = None
                    if not new_head:
                        new_head = last
                test = current
                count = 1
            else:
                count += 1
            current = current.next
        if count <= 1:
            if last:
                last.next = test
            last = test
            if last:
                last.next = None
            if not new_head:
                new_head = last
        return new_head

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
        [1, 2, 3, 3, 4, 4, 5],
        [1, 1, 1, 2, 3],
        [],
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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k < 1:
            return head
        length = 0
        current = head
        tail = None
        while current:
            length += 1
            tail = current
            current = current.next
        if not length or k % length == 0:
            return head
        kk = length - (k % length)
        i = 0
        current = head
        new_head = None
        new_tail = None
        while i < kk:
            i += 1
            new_tail = current
            current = current.next
        new_tail.next = None
        new_head = current
        tail.next = head
        return new_head

def pprint(node):
    while node:
        print node.val,
        if node.next:
            print '->',
        node = node.next
    print ''

def make_list(l):
    node = None
    last = None
    for i in range(len(l), 0, -1):
        node = ListNode(l[i-1])
        node.next = last
        last = node
    return node

def main():
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5, 6], 3),
        ([1, 2, 3, 4, 5], 2),
        ([], 0),
        ([1], 0),
        ([1], 1),
    ]
    for test_case in test_cases:
        l = make_list(test_case[0])
        node = sol.rotateRight(l, test_case[1])
        pprint(node)

if __name__ == "__main__":
    main()

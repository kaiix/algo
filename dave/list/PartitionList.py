class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        l_head = None
        g_head = None
        l_last = None
        g_last = None
        current = head
        while current:
            if current.val < x:
                if l_last:
                    l_last.next = current
                else:
                    l_head = current
                l_last = current
                current = current.next
                l_last.next = None
            else:
                if g_last:
                    g_last.next = current
                else:
                    g_head = current
                g_last = current
                current = current.next
                g_last.next = None
        if g_head:
            if l_last:
                l_last.next = g_head
            else:
                l_head = g_head
        return l_head

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
        ([1, 4, 3, 2, 5, 2], 3),
        ([2, 5, 1, 3, 4], 3),
    ]
    for test_case in test_cases:
        l = make_list(test_case[0])
        node = sol.partition(l, test_case[1])
        pprint(node)

if __name__ == "__main__":
    main()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        front_head = None
        front_tail = None
        middle_head = None
        middle_tail = None
        last = None
        current = head
        i = 1
        while i < m:
            if not front_head:
                front_head = current
            front_tail = current
            current = current.next
            i += 1
        tmp = None
        while i <= n:
            if middle_head:
                tmp = current
                current = current.next
                tmp.next = middle_head
                middle_head = tmp
            else:
                middle_head = current
                middle_tail = current
                current = current.next
                middle_tail.next = None
            i += 1
        if current:
            last = current
        if middle_tail:
            middle_tail.next = last
        if middle_head:
            if front_tail:
                front_tail.next = middle_head
            else:
                front_head = middle_head
        elif last:
            if front_tail:
                front_tail.next = last
            else:
                front_head = last
        return front_head

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
        ([1, 2, 3, 4, 5], 2, 4),
        ([2, 5, 1, 3, 4], 1, 5),
    ]
    for test_case in test_cases:
        l = make_list(test_case[0])
        node = sol.reverseBetween(l, test_case[1], test_case[2])
        pprint(node)

if __name__ == "__main__":
    main()

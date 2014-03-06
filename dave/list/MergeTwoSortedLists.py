class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        new_head = None
        current_1 = l1
        current_2 = l2
        picked = None
        last = None
        while current_1 and current_2:
            if current_1.val < current_2.val:
                picked = current_1
                current_1 = current_1.next
            else:
                picked = current_2
                current_2 = current_2.next
            if last:
                last.next = picked
            picked.next = None
            last = picked
            if not new_head:
                new_head = picked
        if current_1:
            if last:
                last.next = current_1
            else:
                new_head = current_1
        elif current_2:
            if last:
                last.next = current_2
            else:
                new_head = current_2
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
        ([1, 3], [2, 4]),
        ([2, 5], [1, 3, 4]),
    ]
    for test_case in test_cases:
        l1 = make_list(test_case[0])
        l2 = make_list(test_case[1])
        node = sol.mergeTwoLists(l1, l2)
        pprint(node)

if __name__ == "__main__":
    main()

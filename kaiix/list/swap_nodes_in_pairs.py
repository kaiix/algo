#  https://leetcode.com/problems/swap-nodes-in-pairs/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    if not head or not head.next:
        return head
    node = head.next
    tail = node.next
    node.next = head
    head.next = swapPairs(tail)
    return node


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)
    h.next.next.next.next.next = ListNode(6)

    h = swapPairs(h)

    while h:
        print '-->', h.val,
        h = h.next

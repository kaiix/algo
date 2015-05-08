#  https://leetcode.com/problems/remove-linked-list-elements/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head, val):
    sentinel = ListNode(-1)
    sentinel.next = head
    head = sentinel
    prev = head
    current = head.next
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    return head.next


if __name__ == '__main__':
    # Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
    # Return: 1 --> 2 --> 3 --> 4 --> 5

    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(6)
    h.next.next.next = ListNode(3)
    h.next.next.next.next = ListNode(4)
    h.next.next.next.next.next = ListNode(5)
    h.next.next.next.next.next.next = ListNode(6)

    h = removeElements(h, 6)

    while h:
        print '-->', h.val,
        h = h.next

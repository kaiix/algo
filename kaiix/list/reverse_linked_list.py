#  https://leetcode.com/problems/reverse-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    prev, curr = None, head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


def reverseList2(head):
    if not head:
        return head
    elif not head.next:
        return head
    else:
        tail = head.next
        new_head = reverseList2(head.next)
        head.next = tail.next
        tail.next = head
        return new_head


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = ListNode(5)
    h.next.next.next.next.next = ListNode(6)

    h = reverseList2(h)

    while h:
        print '-->', h.val,
        h = h.next

#  https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    head = ListNode(-1)
    prev = head
    carry = 0
    while (l1 or l2):
        total = 0
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        if carry:
            total += carry
        prev.next = ListNode(total % 10)
        carry = total / 10
        prev = prev.next
    if carry:
        prev.next = ListNode(carry)
    return head.next


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)

    l2 = ListNode(9)
#    l2.next = ListNode(9)
#    l2.next.next = ListNode(9)

    result = addTwoNumbers(l1, l2)
    while result:
        print '%d -> ' % result.val,
        result = result.next

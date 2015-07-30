#  https://leetcode.com/problems/palindrome-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'ListNode {}'.format(self.val)


def isPalindrome2(head):
    p = head
    length = 0
    while p:
        p = p.next
        length += 1

    prev, curr = None, head
    for i in xrange(length/2):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    curr = curr.next if length % 2 else curr
    p, q = prev, curr
    while p or q:
        if p.val != q.val:
            return False
        p = p.next
        q = q.next
    return True


def isPalindrome(head):
    if not head:
        return True

    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    tail = reverseList(slow)

    while head and tail:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.next
    return True


def reverseList(head):
    prev, curr = None, head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


def printList(h):
    while h:
        print '-->', h.val,
        h = h.next
    print


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(2)
    h.next.next.next.next = ListNode(1)

    printList(h)
    print isPalindrome(h)

#  https://leetcode.com/problems/intersection-of-two-linked-lists/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def getIntersectionNode2(headA, headB):
    if not headA or not headB:
        return None

    p, q = headA, headB
    while p.next and q.next:
        p = p.next
        q = q.next

    if p.next:
        longer = headA
    else:
        longer = headB
    adv = 0
    while p.next:
        adv += 1
        p = p.next
    while q.next:
        adv += 1
        q = q.next

    if p != q:
        return None

    if longer == headA:
        for _ in xrange(adv):
            headA = headA.next
    else:
        for _ in xrange(adv):
            headB = headB.next
    while headA != headB:
        headA = headA.next
        headB = headB.next
    if headA:
        return headA
    else:
        return None


def getListLength(h):
    length = 0
    while h:
        h = h.next
        length += 1
    return length


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    la, lb = getListLength(headA), getListLength(headB)
    lh = (la - lb) > 0 and headA or headB
    adv = abs(la - lb)
    for _ in xrange(adv):
        lh = lh.next
    if la > lb:
        headA = lh
    else:
        headB = lh
    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA


if __name__ == '__main__':
    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = ListNode(3)
    h2 = ListNode(4)
    h2.next = h1.next.next
    print getIntersectionNode(h1, h2)

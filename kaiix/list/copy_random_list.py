#  https://leetcode.com/submissions/detail/36086814/


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __str__(self):
        return '{}({})'.format(self.label, self.random and self.random.label or None)


def copyRandomList(head):
    node = head
    copied, prev = None, None
    pairs = {}
    while node:
        if not copied:
            prev = RandomListNode(node.label)
            copied = prev
        else:
            prev.next = RandomListNode(node.label)
            prev = prev.next
        pairs[node] = prev
        node = node.next

    node = head
    prev = copied
    while node:
        if node.random:
            prev.random = pairs[node.random]
        node = node.next
        prev = prev.next
    return copied

if __name__ == '__main__':
    h = RandomListNode(2)
    h.random = h
    h.next = RandomListNode(3)
    h.next.random = h
    nh = copyRandomList(h)
    while nh:
        print '->', nh,
        nh = nh.next
    print

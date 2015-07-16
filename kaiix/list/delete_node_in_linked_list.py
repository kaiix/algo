#  https://leetcode.com/problems/delete-node-in-a-linked-list/


def deleteNode(node):
    prev = None
    while node.next:
        prev = node
        node.val = node.next.val
        node = node.next
    if prev:
        prev.next = None

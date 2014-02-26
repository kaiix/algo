# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        try:
            one = head.next
            two = head.next.next
        except:
            return False
        while one and two:
            if one == two:
                return True
            try:
                one = one.next
                two = two.next.next
            except:
                return False
        return False

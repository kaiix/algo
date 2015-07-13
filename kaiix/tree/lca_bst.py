#  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


def lowestCommonAncestor(root, p, q):
    s, l = None, None
    if p.val < q.val:
        s, l = p, q
    else:
        s, l = q, p
    return LCA(root, s, l)


# assume no nodes with same value
def LCA(root, s, l):
    if root.val == s.val or root.val == l.val:
        return root
    elif s.val < root.val and l.val > root.val:
        return root
    elif s.val < root.val and l.val < root.val:
        return LCA(root.left, s, l)
    else:  # s.val > root.val and l.val > root.val
        return LCA(root.right, s, l)

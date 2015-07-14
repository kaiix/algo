#  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'ListNode [%s]' % self.val


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return 'TreeNode [%s]' % self.val


def sortedListToBST(head):
    if head is None:
        return None
    root = createDummyTree(head)
    fillTreeInOrder(root, head)
    return root


def createDummyTree(head):
    root = TreeNode(-1)
    level = [root]
    head = head.next
    while head:
        next_level = []
        for node in level:
            if head:
                node.left = TreeNode(-1)
                head = head.next
                next_level.append(node.left)
            else:
                break
            if head:
                node.right = TreeNode(-1)
                head = head.next
                next_level.append(node.right)
            else:
                break
        level = next_level
    return root


def fillTreeInOrder(root, head):
    node = root
    stk = []
    while stk or node:
        if not node:
            node = stk.pop()
            node.val = head.val
            head = head.next
            node = node.right
        else:
            stk.append(node)
            node = node.left


def printTree(root):
    if not root:
        return

    printTree(root.left)
    print root
    printTree(root.right)


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)

    root = sortedListToBST(head)
    printTree(root)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def levelOrderBFS(root):
    if root is None:
        return
    result = []
    level = [root]
    while level:
        result.append(level)
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
    return result


def levelOrderDFS(root, level, result):
    if root is None:
        return

    if len(result) <= level:
        result.append([])
    result[level].append(root)
    levelOrderDFS(root.left, level+1, result)
    levelOrderDFS(root.right, level+1, result)


def levelOrderDFSStack(root):
    if root is None:
        return []

    result = []
    node, level = root, 0
    stk = []
    while stk or node:
        if not node:
            node, level = stk.pop()
            node, level = node.right, level+1
        else:
            if len(result) <= level:
                result.append([])
            result[level].append(node)
            stk.append((node, level))
            node, level = node.left, level+1
    return result


def levelOrderBFSQueue(root):
    if root is None:
        return []

    result = []
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        if len(result) <= level:
            result.append([])
        result[level].append(node)
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))
    return result


def levelOrderBFSQueue2(root):
    if root is None:
        return []

    result = []
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        if node is None:
            continue
        if len(result) <= level:
            result.append([])
        result[level].append(node)
        queue.append((node.left, level+1))
        queue.append((node.right, level+1))
    return result


def levelOrderBFSStack(root):
    if root is None:
        return []

    result = []
    stk = [(root, 0)]
    while stk:
        node, level = stk.pop()
        if not node:
            continue
        if len(result) <= level:
            result.append([])
        result[level].append(node)
        stk.append((node.right, level+1))
        stk.append((node.left, level+1))
    return result


def levelOrderBFSStack2(root):
    if root is None:
        return []

    result = []
    stk = [(root, 0)]
    while stk:
        node, level = stk.pop()
        if len(result) <= level:
            result.append([])
        result[level].append(node)
        if node.right:
            stk.append((node.right, level+1))
        if node.left:
            stk.append((node.left, level+1))
    return result


def printLevelOrder(levels):
    for r in levels:
        print '[' + ','.join(map(lambda x: str(x.val), r)) + ']'


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print '=== {} ==='.format('bfs')
    result = levelOrderBFS(root)
    printLevelOrder(result)
    print '=== {} ==='.format('dfs')
    result = []
    levelOrderDFS(root, 0, result)
    printLevelOrder(result)
    print '=== {} ==='.format('bfs queue')
    result = levelOrderBFSQueue(root)
    printLevelOrder(result)
    print '=== {} ==='.format('bfs queue 2')
    result = levelOrderBFSQueue2(root)
    printLevelOrder(result)
    print '=== {} ==='.format('bfs stack')
    result = levelOrderBFSStack(root)
    printLevelOrder(result)
    print '=== {} ==='.format('bfs stack 2')
    result = levelOrderBFSStack2(root)
    printLevelOrder(result)
    print '=== {} ==='.format('dfs stack')
    result = levelOrderDFSStack(root)
    printLevelOrder(result)

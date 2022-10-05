from collections import deque


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_iterator(node: Node):
    nodes = [node]

    while nodes:
        yield from nodes

        for no in nodes[:]:
            if no.left:
                nodes.append(no.left)
            if no.right:
                nodes.append(no.right)
            nodes.remove(no)


def tree_by_levels(node):
    return [n.value for n in tree_iterator(node)] if node else []


b = Node(None, None, 10)
a = Node(None, b, 4)
node1 = Node(a, None, 3)
print(node1.value)
print(tree_by_levels(node1))


def tree_by_levels_v2(node: Node):
    if not node:
        return []
    result, queue = [], deque(
        [
            node,
        ]
    )
    while queue:
        no = queue.popleft()
        result.append(no.value)
        if no.left is not None:
            queue.append(no.left)
        if no.right is not None:
            queue.append(no.right)
    return result

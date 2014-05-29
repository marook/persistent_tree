
def in_order_iterator(node):
    if not node is None:
        for child_node in in_order_iterator(node.left):
            yield child_node

        yield node

        for child_node in in_order_iterator(node.right):
            yield child_node

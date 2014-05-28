
def natural_comparator(left, right):
    if left < right:
        return -1

    if right < left:
        return 1

    return 0

class Tree(object):

    def __init__(self, key_comparator=natural_comparator):
        self.key_comparator = key_comparator

        self.root_node = None

    def insert_node(self, inserted_node):
        if self.root_node is None:
            self.root_node = inserted_node

            return

        self.root_node = insert_node_in_tree(self.root_node, inserted_node, self.key_comparator)

def insert_node_in_tree(parent_node, inserted_node, key_comparator):
    cmp_result = key_comparator(parent_node.key, inserted_node.key)

    if cmp_result < 0:
        if parent_node.left is None:
            parent_node.left = inserted_node
        else:
            parent_node.left = insert_node_in_tree(parent_node.left, inserted_node, key_comparator)
    elif cmp_result > 0:
        if parent_node.right is None:
            parent_node.right = inserted_node
        else:
            parent_node.right = insert_node_in_tree(parent_node.right, inserted_node, key_comparator)
    else:
        inserted_node.left = parent_node.left
        inserted_node.right = parent_node.right

        parent_node = inserted_node

    return parent_node

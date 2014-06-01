
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

        self.root_node = self.insert_node_in_tree(self.root_node, inserted_node)

    def insert_node_in_tree(self, parent_node, inserted_node):
        cmp_result = self.key_comparator(parent_node.key, inserted_node.key)

        # insert node 
        if cmp_result < 0:
            if parent_node.left is None:
                parent_node.left = inserted_node
            else:
                parent_node.left = self.insert_node_in_tree(parent_node.left, inserted_node)
        elif cmp_result > 0:
            if parent_node.right is None:
                parent_node.right = inserted_node
            else:
                parent_node.right = self.insert_node_in_tree(parent_node.right, inserted_node)
        else:
            inserted_node.left = parent_node.left
            inserted_node.right = parent_node.right

            parent_node = inserted_node

        # balance tree
        parent_node_balance_factor = parent_node.balance_factor
        if parent_node_balance_factor >= 2:
            if parent_node.left.balance_factor == -1:
                parent_node.left = rotate_node_left(parent_node.left)
        
            parent_node = rotate_node_right(parent_node)
        elif parent_node_balance_factor <= -2:
            if parent_node.right.balance_factor == 1:
                parent_node.right = rotate_node_right(parent_node.right)

            parent_node = rotate_node_left(parent_node)

        return parent_node

def rotate_node_left(parent):
    '''Rotates subtree with the specified parent node to the left.

    Input:
            p
         /     \
       l         r
     /   \     /   \
    ll   lr   rl   rr

    Output:
               r
             /   \
           p       rr
         /   \
       l       rl
     /   \
    ll   lr

    '''

    right = parent.right

    parent.right = right.left
    right.left = parent

    return right

def rotate_node_right(parent):
    left = parent.left

    parent.left = left.right
    left.right = parent

    return left

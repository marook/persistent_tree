from persistent_tree import model, traversals
import unittest

class InOrderIteratorTest(unittest.TestCase):

    def test_iterate_over_tree_nodes_in_order(self):
        parent = create_node(1)
        parent.left = create_node(0)
        parent.right = create_node(2)

        iterated_keys = [node.key for node in traversals.in_order_iterator(parent)]
        self.assertEquals([0, 1, 2], iterated_keys)
        

def create_node(key):
    return model.Node(key, '')

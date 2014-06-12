from persistent_tree import dot, manipulate, model
import unittest

class NaturalComparatorTest(unittest.TestCase):

    def test_compare_strings_with_different_numbers(self):
        self.assertTrue(manipulate.natural_comparator('n0', 'n1') < 0)

    def test_compare_equal_strings(self):
        self.assertEqual(0, manipulate.natural_comparator('n0', 'n0'))

class ManipulateTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = manipulate.Tree()

    def test_insert_root_node_in_tree(self):
        node_key = 0

        self.insert_node_with_key(node_key)

        self.assertEqual(node_key, self.tree.root_node.key)

    def test_insert_two_nodes_in_tree(self):
        self.insert_node_with_key(0)
        self.insert_node_with_key(1)

        self.assertEqual(0, self.tree.root_node.key)
        self.assertEqual(1, self.tree.root_node.right.key)

    def insert_node_with_key(self, key):
        self.tree.insert_node(create_node(key))

    def test_insert_with_same_key_replaces_former_node(self):
        key = 'k0'

        self.tree.insert_node(create_node(key, 'd0'))
        self.tree.insert_node(create_node(key, 'd1'))

        self.assertEqual('d1', self.tree.root_node.data)
        self.assertEqual(None, self.tree.root_node.left)
        self.assertEqual(None, self.tree.root_node.right)

class BalanceTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = manipulate.Tree()

    def test_balance_left_right_case_tree(self):
        '''Balances a tree with three nodes.

        The tree is a 'left right case' as defined in
        http://en.wikipedia.org/wiki/AVL_tree#Insertion
        '''

        self.tree.insert_node(create_node('n5'))
        self.tree.insert_node(create_node('n3'))
        self.tree.insert_node(create_node('n4'))

        self.assertEqual('n3', self.tree.root_node.left.key)
        self.assertEqual('n4', self.tree.root_node.key)
        self.assertEqual('n5', self.tree.root_node.right.key)

    def test_balance_right_case_tree_to_left_case_tree(self):
        self.tree.insert_node(create_node('n4'))
        self.tree.insert_node(create_node('n5'))

        # enable the next line for debugging
        #self.print_tree()

        self.assertEqual('n4', self.tree.root_node.key)
        self.assertEqual('n5', self.tree.root_node.right.key)

    def test_insert_three_nodes_in_unbalanced_order_produces_balanced_tree(self):
        self.tree.insert_node(create_node('n1'))
        self.tree.insert_node(create_node('n2'))
        self.tree.insert_node(create_node('n3'))

        # enable the next line for debugging
        #self.print_tree()

        self.assertEqual('n1', self.tree.root_node.left.key)
        self.assertEqual('n2', self.tree.root_node.key)
        self.assertEqual('n3', self.tree.root_node.right.key)

    def print_tree(self):
        print dot.DotConverter().nodes_to_graph(self.tree.root_node).to_string()
        
class SearchTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = manipulate.Tree()

    def test_searching_tree_for_unknown_key_returns_None(self):
        self.assertEqual(None, self.tree.find_node('k0'))

    def test_searching_tree_for_root_node_key_returns_root_node(self):
        self.tree.insert_node(create_node('n0'))

        self.assertEqual('n0', self.tree.find_node(self.tree.root_node.key).key)

    def test_searching_tree_for_left_leaf_node_key_returns_leaf_node(self):
        self.tree.insert_node(create_node('n0'))
        self.tree.insert_node(create_node('n1'))
        self.tree.insert_node(create_node('n2'))

        self.assertEqual('n0', self.tree.find_node('n0').key)

class RotateNodeLeftTest(unittest.TestCase):

    def test_rotate_fails_when_there_is_no_right_child_node(self):
        parent = create_node('n0')

        self.assertRaises(Exception, manipulate.rotate_node_left, parent)

    def test_rotate_left_child_node_assignments(self):
        nodes = create_height_2_tree()

        manipulate.rotate_node_left(nodes['p'])

        # first test the edges affected by the rotation
        self.assertEqual(nodes['p'], nodes['r'].left)
        self.assertEqual(nodes['rl'], nodes['p'].right)

        # then test that the other edges are still the same
        self.assertEquals(nodes['l'], nodes['p'].left)
        self.assertEquals(nodes['rr'], nodes['r'].right)

    def test_node_heights_after_rotate_left(self):
        nodes = create_height_2_tree()

        # first we make sure that the nodes have the correct initial heights
        self.assert_node_heights(nodes, {
                'p': 3,

                'r': 2,
                'rl': 1,
                'rr': 1,

                'l': 2,
                'll': 1,
                'lr': 1,
                })

        manipulate.rotate_node_left(nodes['p'])

        # after the rotation we check the heights
        self.assert_node_heights(nodes, {
                'p': 3,

                'r': 4,
                'rl': 1,
                'rr': 1,

                'l': 2,
                'll': 1,
                'lr': 1,
                })

    def assert_node_heights(self, nodes, expected_node_heights):
        for node_key, expected_node_height in expected_node_heights.iteritems():
            node_height = nodes[node_key].height

            self.assertEqual(expected_node_height, node_height, '%s should have height %s but has %s' % (node_key, expected_node_height, node_height))
        
def create_height_2_tree():
    '''Creates a tree with height 2

            p
         /     \
       l         r
     /   \     /   \
    ll   lr   rl   rr
    '''

    p = create_node('p')
    
    l = create_node('l')
    ll = create_node('ll')
    lr = create_node('lr')
    
    r = create_node('r')
    rl = create_node('rl')
    rr = create_node('rr')

    p.left = l
    p.right = r

    l.left = ll
    l.right = lr

    r.left = rl
    r.right = rr

    return {
        'p': p,

        'l': l,
        'll': ll,
        'lr': lr,

        'r': r,
        'rl': rl,
        'rr': rr,
        }
    
def create_node(key, data=''):
    return model.Node(key, data)

if __name__ == '__main__':
    unittest.main()

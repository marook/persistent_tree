from persistent_tree import dot, manipulate, model
import unittest

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
        self.assertEqual(1, self.tree.root_node.left.key)

    def insert_node_with_key(self, key):
        self.tree.insert_node(create_node(key))
        

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

        self.assertEqual('n5', self.tree.root_node.left.key)
        self.assertEqual('n4', self.tree.root_node.key)
        self.assertEqual('n3', self.tree.root_node.right.key)

    def test_balance_right_case_tree_to_left_case_tree(self):
        self.tree.insert_node(create_node('n4'))
        self.tree.insert_node(create_node('n5'))

        print dot.DotConverter().nodes_to_graph(self.tree.root_node).to_string()

        self.assertEqual('n5', self.tree.root_node.left.key)
        self.assertEqual('n4', self.tree.root_node.key)

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
            self.assertEqual(expected_node_height, nodes[node_key].height)
        
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
    

def create_node(key):
    return model.Node(key, '')

if __name__ == '__main__':
    unittest.main()

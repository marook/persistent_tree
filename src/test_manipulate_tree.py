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

def create_node(key):
    return model.Node(key, '')

if __name__ == '__main__':
    unittest.main()

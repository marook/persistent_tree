from persistent_tree import manipulate, model
import unittest

class ManipulateTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = manipulate.Tree()

    def test_insert_root_node_in_tree(self):
        node_key = 0

        self.tree.insert_node(create_node(node_key))

        self.assertEqual(node_key, self.tree.root_node.key)

    def test_insert_two_nodes_in_tree(self):
        self.tree.insert_node(create_node(0))
        self.tree.insert_node(create_node(1))

        self.assertEqual(0, self.tree.root_node.key)
        self.assertEqual(1, self.tree.root_node.left.key)

def create_node(key):
    return model.Node(key, '')

if __name__ == '__main__':
    unittest.main()

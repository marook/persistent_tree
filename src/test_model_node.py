#!/usr/bin/python2

from persistent_tree import model
import unittest

class NodeWeightTest(unittest.TestCase):

    def test_that_single_node_has_weight_1(self):
        self.assertEqual(1, create_node().weight)

class NodeHeightTest(unittest.TestCase):

    def test_that_single_node_has_height_1(self):
        self.assertEqual(1, create_node().height)

    def test_that_balanced_three_node_tree_has_height_2(self):
        parent = create_node()
        parent.left = create_node()
        parent.right = create_node()
        
        self.assertEqual(2, parent.height)

class NodeEqualsTest(unittest.TestCase):

    def setUp(self):
        self.n1 = create_node()
        self.n2 = create_node()

    def test_that_same_values_make_nodes_equal(self):
        self.assert_nodes_equal()

    def test_that_different_key_make_nodes_unequal(self):
        self.n2.key = 'other_key'

        self.assert_nodes_not_equal()

    def assert_nodes_equal(self):
        self.assertEqual(self.n1, self.n2)

    def assert_nodes_not_equal(self):
        self.assertFalse(self.n1 == self.n2)

def create_node():
    return model.Node('key', 'value')

if __name__ == '__main__':
    unittest.main()

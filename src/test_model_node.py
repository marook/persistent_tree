#!/usr/bin/python2

from persistent_tree import model
import unittest

class NodeWeightTest(unittest.TestCase):

    def test_that_single_node_has_weight_1(self):
        self.assertEqual(1, create_node().weight)

class NodeEqualsTest(unittest.TestCase):

    def test_that_same_values_make_nodes_equal(self):
        n1 = create_node()
        n2 = create_node()

        self.assertEqual(n1, n2)

def create_node():
    return model.Node('key', 'value')

if __name__ == '__main__':
    unittest.main()

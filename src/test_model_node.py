#!/usr/bin/python2

from persistent_tree import model
import unittest

class ModelWeightTest(unittest.TestCase):

    def test_that_single_node_has_weight_1(self):
        self.assertEqual(1, create_node().weight)

def create_node():
    return model.Node('key', 'value')

if __name__ == '__main__':
    unittest.main()

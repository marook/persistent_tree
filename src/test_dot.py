from persistent_tree import dot, model
import unittest

class DotConverterTest(unittest.TestCase):

    def setUp(self):
        self.converter = dot.DotConverter()

    def test_convert_two_node_tree(self):
        parent = create_node('1')
        parent.left = create_node('0')

        graph = self.converter.nodes_to_graph(parent)

        # TODO make this test independent of graph formatting
        self.assertEqual('digraph G {\n0 -> 1;\n}\n', graph.to_string())

def create_node(key):
    return model.Node(key, '')

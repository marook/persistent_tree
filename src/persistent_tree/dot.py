
from persistent_tree import traversals
import pydot

def identity_formatter(value):
    return value

class DotConverter(object):

    def __init__(self, key_to_id=identity_formatter):
        self.key_to_id = key_to_id

    def nodes_to_graph(self, root_node):
        graph = pydot.Graph()
        graph.set_type('digraph')

        self.append_subtree_to_graph(graph, root_node)

        return graph

    def append_subtree_to_graph(self, graph, root_node):
        for node in traversals.in_order_iterator(root_node):
            node_id = self.key_to_id(node.key)

            left_node = node.left
            if not left_node is None:
                self.append_edge_from_node_to_id(graph, left_node, node_id)

            right_node = node.right
            if not right_node is None:
                self.append_edge_from_node_to_id(graph, right_node, node_id)

    def append_edge_from_node_to_id(self, graph, src_node, dst_node_id):
        src_node_id = self.key_to_id(src_node.key)

        graph.add_edge(pydot.Edge(src_node_id, dst_node_id))

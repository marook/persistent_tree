from persistent_tree import manipulate, model

class FixedNodeSizeWriter(object):

    def __init__(self, key_size, data_size):
        self.key_size = key_size
        self.data_size = data_size

        self.node_size = self.key_size + self.data_size

    def write_nodes(self, f, root_node):
        self.write_nodes_subtree(f, 0, root_node)

    def write_nodes_subtree(self, f, node_index, subtree_node):
        self.assert_valid_node_size(subtree_node)

        self.seek_node(f, node_index)

        f.write(subtree_node.key)
        f.write(subtree_node.data)

        left_node = subtree_node.left
        if not left_node is None:
            self.write_nodes_subtree(f, 2 * node_index + 1, left_node)

        right_node = subtree_node.right
        if not right_node is None:
            self.write_nodes_subtree(f, 2 * node_index + 2, right_node)

    def assert_valid_node_size(self, node):
        self.assert_valid_key_size(node.key)
        self.assert_valid_data_size(node.data)

    def assert_valid_key_size(self, key):
        if len(key) != self.key_size:
            raise IllegalKeySizeException()

    def assert_valid_data_size(self, data):
        if len(data) != self.data_size:
            raise IllegalDataSizeException()

    def seek_node(self, f, node_index):
        seek_fixed_size_node(f, node_index, self.node_size)

class IllegalNodeSizeException(Exception):
    pass

class IllegalKeySizeException(IllegalNodeSizeException):
    pass

class IllegalDataSizeException(IllegalNodeSizeException):
    pass

class FixedNodeSizeReader(object):

    def __init__(self, key_size, data_size, key_comparator=manipulate.natural_comparator):
        self.key_size = key_size
        self.data_size = data_size

        self.node_size = self.key_size + self.data_size

        self.key_comparator = key_comparator

    def find_node(self, f, lookup_key):
        return self.find_node_in_subtree(f, lookup_key, 0)

    def find_node_in_subtree(self, f, lookup_key, subtree_node_index):
        subtree_node_key = self.read_key(f, subtree_node_index)

        cmp_result = self.key_comparator(lookup_key, subtree_node_key)

        if cmp_result == 0:
            subtree_node_data = self.read_data_at_current_pos(f)

            # we use lookup_key instead of subtree_node_key so the
            # number of references to subtree_node_key is 0 and so
            # subtree_node_key can be garbage collected
            return model.Node(lookup_key, subtree_node_data)

        # release subtree_node_key for garbage collection
        subtree_node_key = None

        if cmp_result < 0:
            return self.find_node_in_subtree(f, lookup_key, 2 * subtree_node_index + 1)
        else:
            return self.find_node_in_subtree(f, lookup_key, 2 * subtree_node_index + 2)

    def read_key(self, f, node_index):
        self.seek_node(f, node_index)

        return f.read(self.key_size)

    def read_data_at_current_pos(self, f):
        return f.read(self.data_size)

    def seek_node(self, f, node_index):
        seek_fixed_size_node(f, node_index, self.node_size)

def seek_fixed_size_node(f, node_index, node_size):
    f.seek(node_index * node_size)

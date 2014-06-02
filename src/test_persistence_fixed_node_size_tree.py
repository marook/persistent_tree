
from persistent_tree import model, persistence
import tempfile
import unittest

class WriteAndFindNodeInFixedNodeSizeTreeTest(unittest.TestCase):

    def setUp(self):
        self.file = tempfile.TemporaryFile(mode='w+b')

        self.key_size = 1
        self.data_size = 2

        self.writer = persistence.FixedNodeSizeWriter(self.key_size, self.data_size)
        self.reader = persistence.FixedNodeSizeReader(self.key_size, self.data_size)

        self.persisted_root_node = None

    def tearDown(self):
        self.file.close()

    def test_write_and_find_one_node(self):
        self.persisted_root_node = create_node('0')

        self.write_nodes()

        self.assertEqual(self.persisted_root_node, self.find_node('0'))

    def test_find_no_node_in_empty_file(self):
        self.write_nodes()

        self.assertEqual(None, self.find_node('0'))

    def test_write_and_find_leaf_node(self):
        leaf_node = create_node('0')

        self.persisted_root_node = create_node('1')
        self.persisted_root_node.left = leaf_node

        self.write_nodes()

        self.assertEqual(leaf_node, self.find_node('0'))

    def test_find_zero_key_node_raises_IllegalKeyException(self):
        '''The FixedNodeSizeTree does not support 'zero' keys.

        A key with just \0 bytes markes an not set leaf node.
        '''

        self.write_nodes()

        self.assertRaises(persistence.IllegalKeyValueException, self.find_node, '\x00')

    def test_write_not_set_key_node_fails_with_IllegalKeyValueException(self):
        self.persisted_root_node = create_node('\x00')

        self.assertRaises(persistence.IllegalKeyValueException, self.write_nodes)

    def write_nodes(self):
        self.writer.write_nodes(self.file, self.persisted_root_node)

        self.reset_file_position()

    def reset_file_position(self):
        self.file.seek(0)

    def find_node(self, lookup_key):
        return self.reader.find_node(self.file, lookup_key)

def create_node(key):
    return model.Node(key, 'd%s' % (key, ))

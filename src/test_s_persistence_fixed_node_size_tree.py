
from persistent_tree import model, persistence, manipulate
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

    def test_write_and_find_left_leaf_node(self):
        leaf_node = create_node('0')

        self.persisted_root_node = create_node('1')
        self.persisted_root_node.left = leaf_node

        self.write_nodes()

        self.assertEqual(leaf_node, self.find_node(leaf_node.key))

    def test_write_and_find_right_leaf_node(self):
        leaf_node = create_node('1')

        self.persisted_root_node = create_node('0')
        self.persisted_root_node.right = leaf_node

        self.write_nodes()

        self.assertEqual(leaf_node, self.find_node(leaf_node.key))

    def test_find_zero_key_node_raises_IllegalKeyException(self):
        '''The FixedNodeSizeTree does not support 'zero' keys.

        A key with just \0 bytes markes an not set leaf node.
        '''

        self.write_nodes()

        self.assertRaises(persistence.IllegalKeyValueException, self.find_node, '\x00')

    def test_write_not_set_key_node_fails_with_IllegalKeyValueException(self):
        self.persisted_root_node = create_node('\x00')

        self.assertRaises(persistence.IllegalKeyValueException, self.write_nodes)

    def test_write_and_find_many_nodes(self):
        tree = manipulate.Tree()

        for key in alphabet():
            node = create_node(key)

            tree.insert_node(node)

        self.persisted_root_node = tree.root_node

        self.write_nodes()

        for key in alphabet():
            self.assertTrue(not self.find_node(key) is None, 'Missing node with key %s' % (key,))

    def write_nodes(self):
        self.writer.write_nodes(self.file, self.persisted_root_node)

        self.reset_file_position()

    def reset_file_position(self):
        self.file.seek(0)

    def find_node(self, lookup_key):
        return self.reader.find_node(self.file, lookup_key)

class GetLeftNodeIndexTest(unittest.TestCase):

    def test_0_node_left_index_is_1(self):
        self.assertEqual(1, persistence.get_left_node_index(0))

    def test_1_node_left_index_is_3(self):
        self.assertEqual(3, persistence.get_left_node_index(1))

    def test_2_node_left_index_is_5(self):
        self.assertEqual(5, persistence.get_left_node_index(2))

class GetRightNodeIndexTest(unittest.TestCase):

    def test_0_node_right_index_is_2(self):
        self.assertEqual(2, persistence.get_right_node_index(0))

    def test_1_node_right_index_is_4(self):
        self.assertEqual(4, persistence.get_right_node_index(1))

    def test_2_node_right_index_is_6(self):
        self.assertEqual(6, persistence.get_right_node_index(2))

def create_node(key):
    return model.Node(key, 'd%s' % (key, ))

def alphabet():
    for key_ord in xrange(ord('a'), ord('z')):
        yield chr(key_ord)


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
        self.persisted_root_node = model.Node('0', 'd0')

        self.writer.write_nodes(self.file, self.persisted_root_node)

        self.reset_file_position()

        found_node = self.reader.find_node(self.file, '0')

        self.assertEqual(self.persisted_root_node, found_node)

    def reset_file_position(self):
        self.file.seek(0)


def natural_comparator(left, right):
    if left < right:
        return -1

    if right < left:
        return 1

    return 0

class Tree(object):

    def __init__(self, key_comparator=natural_comparator):
        self.key_comparator = key_comparator

        self.root_node = None

    def insert_node(self, inserted_node):
        self.root_node = inserted_node

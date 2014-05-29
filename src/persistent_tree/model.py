
class Node(object):

    def __init__(self, key, data):
        self.key = key
        self.data = data

        self.left = None
        self.right = None

    @property
    def weight(self):
        weight = 1

        if not self.left is None:
            weight += self.left.weight

        if not self.right is None:
            weight += self.right.weight

        return weight

    @property
    def height(self):
        max_child_height = 0

        if not self.left is None:
            max_child_height = max(max_child_height, self.left.height)

        if not self.right is None:
            max_child_height = max(max_child_height, self.right.height)

        return max_child_height + 1
        
    @property
    def balance_factor(self):
        '''Balance factor as defined in an AVL tree.

        For more details see
        http://en.wikipedia.org/wiki/AVL_tree#Insertion
        '''

        height_left = 0 if self.left is None else self.left.height
        height_right = 0 if self.right is None else self.right.height

        return height_left - height_right

    def __eq__(self, other):
        return self.key == other.key and self.data == other.data and self.left == other.left and self.right == other.right

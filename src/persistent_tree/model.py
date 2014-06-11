
class Node(object):

    __slots__ = ['key', 'data', 'parent', '_left', '_right', 'height']

    def __init__(self, key, data):
        self.key = key
        self.data = data

        self.parent = None
        self._left = None
        self._right = None

        self.height = 1

    @property
    def weight(self):
        weight = 1

        if not self.left is None:
            weight += self.left.weight

        if not self.right is None:
            weight += self.right.weight

        return weight

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, new_left):
        if not self.left is None:
            self.left.parent = None

        self._left = new_left

        if not self.left is None:
            self.left.parent = self

        self._update_height()

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, new_right):
        if not self.right is None:
            self.right.parent = None

        self._right = new_right

        if not self.right is None:
            self.right.parent = self

        self._update_height()

    def _update_height(self):
        former_height = self.height

        height = 1

        if not self.left is None:
            height = self.left.height + 1

        if not self.right is None:
            right_height = self.right.height + 1

            if right_height > height:
                height = right_height

        if former_height == height:
            return

        self.height = height

        if not self.parent is None:
            self.parent._update_height()
        
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


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

    def __eq__(self, other):
        return self.key == other.key and self.data == other.data and self.left == other.left and self.right == other.right

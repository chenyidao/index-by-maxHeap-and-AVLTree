
class AVLTreeNode:
    """
    The node class of the AVL tree, used to represent the nodes of the AVL tree
    """
    def __init__(self, key, value, height=0, left=None, right=None):
        """
        Init an AVL node
        :param key:used to sort
        :param value:
        :param height: The height of this node in the tree
        :param left: Left child
        :param right: Right child
        """
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __str__(self):
        """
        :return: A string contains the instance's info.
        """
        return "<class AVLNode>[ key: " + str(self.key) + ", value: " + str(self.value) + ", left: " + str(self.left) \
               + ", right: " + str(self.right) + ", height " + str(self.height) + " ]"


class AVLTreeMap:
    """An AVL tree in disguise, where the nodes in the tree contain“key-value” pairs.
    You place items in the tree ordered by their key, and this key has an associated
    value tagging along with it. The key can be any reference type (e.g., integer or string),
     and so can the value (e.g., list).
     Attributes:
         root： The root of the AVL tree
    """
    ALLOWED_IMBALANCE = 1

    def __init__(self):
        self.root = None

    def search_path(self):
        """
        Use pre-order traversal to return a list of all the keys in the tree
        :return: The list which contains all the keys in pre-order traversing.
        """
        return self.search_path_recursive(self.root)

    def get(self, key):
        """
        Get the value corresponding to the given key from the tree, if the given key is not in the tree, return None
        :return: Null if the key isn’t in the tree, or the associated value if it is
        """
        return self.get_recursive(key, self.root)

    def put(self, key, value):
        """
        Add the given key-value pair to the tree, if the given key already exists in the tree, update
        :return: Null if the key isn’t in the tree, or the associated value if it is
        """
        self.root = self.put_recursive(key, value, self.root)
        return self.root

    def print(self):
        self.print_recursive(self.root)

    def search_path_recursive(self, curr_node):
        if curr_node is None:
            return []
        node_list = [curr_node.key]
        node_list += self.search_path_recursive(curr_node.left)
        node_list += self.search_path_recursive(curr_node.right)
        return node_list

    def get_recursive(self, key, curr_node):
        if curr_node is None:
            return None
        if key == curr_node.key:
            return curr_node.value
        elif key > curr_node.key:
            return self.get_recursive(key, curr_node.right)
        else:
            return self.get_recursive(key, curr_node.left)

    def put_recursive(self, key, value, curr_node=None):
        if curr_node is None:
            return AVLTreeNode(key, value)

        new_node = AVLTreeNode(key, value)

        if new_node == curr_node:
            curr_node.value = new_node.value
        elif new_node > curr_node:
            curr_node.right = self.put_recursive(key, value, curr_node.right)
        else:
            curr_node.left = self.put_recursive(key, value, curr_node.left)
        return self.balance(curr_node)

    def print_recursive(self, curr_node):
        print(curr_node)
        if curr_node is None:
            return
        else:
            self.print_recursive(curr_node.left)
            self.print_recursive(curr_node.right)

    def balance(self, curr_node):
        if curr_node is None:
            return curr_node
        if self.height(curr_node.left) - self.height(curr_node.right) > AVLTreeMap.ALLOWED_IMBALANCE:
            if self.height(curr_node.left.left) >= self.height(curr_node.left.right):
                curr_node = self.rotate_with_left_child(curr_node)
            else:
                curr_node = self.double_with_left_child(curr_node)
        elif self.height(curr_node.right) - self.height(curr_node.left) > AVLTreeMap.ALLOWED_IMBALANCE:
            if self.height(curr_node.right.right) >= self.height(curr_node.right.left):
                curr_node = self.rotate_with_right_child(curr_node)
            else:
                curr_node = self.double_with_right_child(curr_node)

        curr_node.height = max(self.height(curr_node.left), self.height(curr_node.right)) + 1
        return curr_node

    def double_with_left_child(self, curr_node):
        curr_node.left = self.rotate_with_right_child(curr_node.left)
        return self.rotate_with_left_child(curr_node)

    def double_with_right_child(self, curr_node):
        curr_node.right = self.rotate_with_left_child(curr_node.right)
        return self.rotate_with_right_child(curr_node)

    def rotate_with_left_child(self, curr_node):
        new_root = curr_node.left
        curr_node.left = new_root.right
        new_root.right = curr_node
        curr_node.height = max(self.height(curr_node.left), self.height(curr_node.right)) + 1
        new_root.height = max(self.height(new_root.left), self.height(new_root.right)) + 1
        return new_root

    def rotate_with_right_child(self, curr_node):
        new_root = curr_node.right
        curr_node.right = new_root.left
        new_root.left = curr_node
        curr_node.height = max(self.height(curr_node.left), self.height(curr_node.right)) + 1
        new_root.height = max(self.height(new_root.left), self.height(new_root.right)) + 1
        return new_root

    def height(self, curr_node):
        return -1 if curr_node is None else curr_node.height


if __name__ == '__main__':
    tree = AVLTreeMap()
    tree.put(15, "bob")
    tree.put(20, "anna")
    tree.put(24, "tom")
    tree.put(10, "david")
    tree.put(13, "david")
    tree.put(7, "ben")
    tree.put(30, "karen")
    tree.put(36, "erin")
    tree.put(25, "david")
    tree.put(13, "nancy")

    print(tree.get(13))
    print(tree.get(36))
    print(tree.get(7))
    print(tree.search_path())







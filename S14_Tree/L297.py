# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def tree_count(node):
            if not node:
                return 0
            else:
                return 1 + tree_count(node.left) + tree_count(node.right)

        Tn = tree_count(root)
        result = []
        Q = deque()
        Q.append(root)
        Ti = 0
        while Q:
            node = Q.popleft()
            if not node:
                if Ti == Tn:
                    break
                result.append('#')
            else:
                Ti += 1
                result.append(str(node.val))
                if Ti < Tn:
                    Q.append(node.left)
                    Q.append(node.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def decode(val):
            if val:
                return TreeNode(val)
            else:
                return None

        n = len(data)
        if n == 0:
            return None
        root = TreeNode(data[0])
        Q = deque()
        Q.append(root)
        ind = 0
        while ind < n - 1:
            node = Q.popleft()
            if node:
                node.left = TreeNode(data[ind + 1])
                if ind + 2 < n:
                    node.right = TreeNode(data[ind + 2])
                Q.append(node.left)
                Q.append(node.right)
                ind += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

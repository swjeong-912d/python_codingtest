class TrieNode:
    def __init__(self, val=0):
        self.isWord = val
        self.children = {}

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(False)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children.keys():
                node.children[c] = TrieNode(False)
            node = node.children[c]
        node.isWord = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c in node.children.keys():
                node = node.children[c]
            else:
                return False
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c in node.children.keys():
                node = node.children[c]
            else:
                return False
        return True
def print_test():
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    param_3 = obj.startsWith('a')
    print (param_3)
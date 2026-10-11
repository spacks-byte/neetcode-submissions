class PrefixTree:
    class TreeNode():
        def __init__(self):
            self.end = False
            self.children = {}

    def __init__(self):
        self.root = self.TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if not current.children.get(letter, 0):
                current.children[letter] = self.TreeNode()
            current = current.children[letter]
        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if not current.children.get(letter, 0):
                return False
            current = current.children[letter]
        if current.end == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if not current.children.get(letter, 0):
                return False
            current = current.children[letter]
        return True
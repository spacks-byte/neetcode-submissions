class WordDictionary:
    class TreeNode():
        def __init__(self):
            self.end = False
            self.children = {}

    def __init__(self):
        self.root = self.TreeNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if not current.children.get(letter, 0):
                current.children[letter] = self.TreeNode()
            current = current.children[letter]
        current.end = True

    def search(self, word: str) -> bool:
        return self.endsWith(self.root, word)

    def endsWith(self, root, word: str) -> bool:
        current = root
        if len(word):
            letter = word[0]
            if letter == ".":
                for child in current.children.values():
                    dot = self.endsWith(child, word[1:])
                    if dot:
                        return True
                return False
            else:
                if not current.children.get(letter, 0):
                    return False
                current = current.children[letter]
                return self.endsWith(current, word[1:])

        if current.end == True:
            return True
        return False
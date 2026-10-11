from trie import Trie

class Storage:
    def __init__(self):
        self.trie = Trie()

    def add(self, word, original_word: str = None):
        self.trie.insert(word, original_word)

    def searchByPrefix(self, prefix):
        return self.trie.searchByPrefix(prefix)

    def contains(self, word):
        return self.trie.contains(word)

    def getAllWords(self):
        return self.trie.getAllWords()
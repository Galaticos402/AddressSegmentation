from trie import Trie

class Storage:
    def __init__(self):
        self.trie = Trie()
        self.max_word_length = 0

    def add(self, word, original_word: str = None):
        self.trie.insert(word, original_word)

    def searchByPrefix(self, prefix):
        return self.trie.searchByPrefix(prefix)

    def contains(self, word):
        return self.trie.contains(word)

    def getAllWords(self):
        return self.trie.getAllWords()
    
    def fuzzyContains(self, word: str) -> list[str]:
        return self.trie.fuzzyContains(word)
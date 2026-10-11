class Node:
    def __init__(self, value: str, is_terminated = False):
        self.val = value
        self.children = {}
        self.is_terminated = is_terminated
        self.original_word = None

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str, original_word: str = None):
        ite = self.root
        for c in word:
            if c not in ite.children:
                ite.children[c] = Node(c)
            ite = ite.children[c]
        ite.is_terminated = True
        ite.original_word = original_word

    def contains(self, word: str):
        ite = self.root
        for c in word:
            if c not in ite.children:
                return None
            ite = ite.children[c]
        if ite.is_terminated and ite.original_word is not None:
            return ite.original_word 
        return None

    def searchByPrefix(self, prefix: str) -> list[str]:
        ite = self.root
        for c in prefix:
            if c not in ite.children:
                # Prefix not found in Trie, therefore return empty
                return []
            ite = ite.children[c]
        viable_options = self._dfs(ite)
        result = [prefix + word for word in viable_options]
        return result

    def getAllWords(self) -> list[str]:
        return self._dfs(self.root)

    def _dfs(self, node: Node) -> list[str]:
        result: list[str] = []
        stack: list[dict] = []

        stack.append({
            "node": node,
            "word": ""
        })

        while len(stack) > 0:
            item = stack.pop()

            current_node = item["node"]
            current_word = item["word"]

            if current_node.is_terminated:
                result.append(current_word)

            for letter, child in current_node.children.items():
                stack.append({
                    "node": child,
                    "word": current_word + letter
                })

        return result


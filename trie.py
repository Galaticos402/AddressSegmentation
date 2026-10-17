from collections import deque
import queue


class Node:
    def __init__(self, value: str, is_terminated = False):
        self.val = value
        self.children = {}
        self.is_terminated = is_terminated
        self.original_word = None

class Trie:
    def __init__(self):
        self.root = Node(None)
        self.max_word_length = 0

    def insert(self, word: str, original_word: str = None):
        ite = self.root
        for c in word:
            if c not in ite.children:
                ite.children[c] = Node(c)
            ite = ite.children[c]
        ite.is_terminated = True
        ite.original_word = original_word
        self.max_word_length = max(
            self.max_word_length,
            len(word)
        )

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

    def fuzzyContains(self, word: str) -> list[str]:
        
        ite = self.root
        for c in word:
            if c not in ite.children:
                break
            ite = ite.children[c]
        if ite.is_terminated and ite.original_word is not None:
            return [ite.original_word] 
        
        max_distance = 2
        n = len(word)
        results = []
        initial_row = list(range(n + 1))

        dp: dict[str, dict[str, int]] = {}
        
        # Handle root node 
        initial_row = list(range(n + 1))
        dp[""] = {j: initial_row[j] for j in range(n + 1)}

        queue = deque([(self.root, "")])
        
        while queue:
            current_node, current_prefix = queue.popleft()
            current_row = dp[current_prefix]

            if current_node.is_terminated:
                if current_row[n] == 0:
                    return [current_node.original_word]

                if current_row[n] <= max_distance:
                    results.append(current_node.original_word)

            for letter, child in current_node.children.items():
                next_prefix = current_prefix + letter
                next_row = [current_row[0] + 1]

                for j in range(1, n + 1):
                    insert_cost = next_row[j - 1] + 1
                    delete_cost = current_row[j] + 1
                    replace_cost = current_row[j - 1] + (0 if word[j - 1] == letter else 1)
                    next_row.append(min(insert_cost, delete_cost, replace_cost))

                dp[next_prefix] = {j: next_row[j] for j in range(n + 1)}

                if min(next_row) <= max_distance:
                    queue.append((child, next_prefix))
        return max(results, key=lambda x: len(x)) if results else []
        
            
        
        

from collections import deque

from trie import Trie
import unicodedata
import re
class SentenceProcessor:
    def __init__(self):
        pass
        
    def normalize(self, sentence: str):
        sentence = sentence.lower()
        sentence = sentence.replace("Đ", "D").replace("đ", "d")
        sentence = unicodedata.normalize("NFD", sentence)
        sentence = "".join(c for c in sentence if unicodedata.category(c) != "Mn")
        sentence = re.sub(r"[^a-zA-Z0-9]", "", sentence)
        return sentence
     
    
    def possibleMatches(self, s: str, trie: Trie):
        matches = []
        size = len(s)
        max_distance = 2

        for start in range(size):
            max_length = min(
                size - start,
                trie.max_word_length + max_distance
            )

            initial_row = list(range(max_length + 1))
            queue = deque([(trie.root, initial_row)])

            while queue:
                node, previous_row = queue.popleft()

                for letter, child in node.children.items():
                    current_row = [previous_row[0] + 1]

                    for j in range(1, max_length + 1):
                        insert_cost = current_row[j - 1] + 1
                        delete_cost = previous_row[j] + 1
                        replace_cost = previous_row[j - 1] + (
                            s[start + j - 1] != letter
                        )

                        current_row.append(
                            min(insert_cost, delete_cost, replace_cost)
                        )

                    # Check every non-empty substring ending at this position
                    if child.is_terminated:
                        for end in range(1, max_length + 1):
                            if current_row[end] <= max_distance:
                                matches.append({
                                    "word": s[start:start + end],
                                    "original_word": child.original_word,
                                })

                    # Prune branches that cannot produce a valid match
                    if min(current_row) <= max_distance:
                        queue.append((child, current_row))

        return [max(matches, key=lambda x: len(x["word"]))] if matches else []
        # matches = []

        # size = len(s)

        # for i in range(size + 1):
        #     for j in range(i):
        #         possible_words = trie.fuzzyContains(s[j:i])
        #         if len(possible_words) > 0:
        #             matches.append({
        #                 "word": s[j:i],
        #                 "original_word": possible_words[0],
        #             })
        # # print(f"Possible matches for {s}: {matches}")
        # return matches

    def getMostReasonableCombination(self, matches: list[dict], s: str):
        highest_match = matches[0] if matches else {"province": None, "ward": None, "street": None}
        highest_match_score = 0
        for match in matches:
            score = 0
            score = score + 1 if match["province"] is not None else score
            score = score + 1 if match["ward"] is not None else score
            score = score + 1 if match["street"] is not None else score
            if score > highest_match_score:
                highest_match_score = score
                highest_match = match
        return highest_match

    def _dfs(self, trace_map, key, s, curr_path: list, all_paths: list[list]):
        if key == len(s):
            all_paths.append(curr_path.copy())
            return

        if key not in trace_map:
            all_paths.append(curr_path.copy())
            return

        for vertex in trace_map[key]:
            curr_path.append(s[key:vertex])

            self._dfs(
                trace_map,
                vertex,
                s,
                curr_path,
                all_paths
            )

            curr_path.pop()
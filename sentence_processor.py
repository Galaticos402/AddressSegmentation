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
        dp = [False] * (size + 1)
        dp[0] = True

        for i in range(size + 1):
            for j in range(i):
                if dp[j] and trie.contains(s[j:i]) is not None:
                    matches.append({
                        "word": s[j:i],
                        "original_word": trie.contains(s[j:i]),
                    })
                    dp[i] = True

        return list(matches)

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
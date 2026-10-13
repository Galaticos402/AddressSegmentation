class TypoGenerator:
    def __init__(self):
        self.typo_dict = {
            "0": ["o"],
            "o": ["0"],
            "1": ["l", "i"],
            "l": ["1"],
            "i": ["1"],
            "5": ["s"],
            "s": ["5"],
            "8": ["b"],
            "b": ["8"],
        }
    
    def generate_typos(self, s: str):
        typos = set()
        for i, char in enumerate(s):
            if char in self.typo_dict:
                for typo_char in self.typo_dict[char]:
                    typo = s[:i] + typo_char + s[i+1:]
                    typos.add(typo)
        return typos
from typing import Dict, List


class AlphabetTeacher:
    """Teaches Russian alphabet with rows and mnemonics."""

    def __init__(self) -> None:
        self.alphabet = [
            "А",
            "Б",
            "В",
            "Г",
            "Д",
            "Е",
            "Ё",
            "Ж",
            "З",
            "И",
            "Й",
            "К",
            "Л",
            "М",
            "Н",
            "О",
            "П",
            "Р",
            "С",
            "Т",
            "У",
            "Ф",
            "Х",
            "Ц",
            "Ч",
            "Ш",
            "Щ",
            "Ъ",
            "Ы",
            "Ь",
            "Э",
            "Ю",
            "Я",
        ]
        self.rows = {
            "basic": [
                ltr for ltr in self.alphabet if ltr not in ["Ё", "Ъ", "Ь", "Ы", "Э", "Ю", "Я"]
            ],
            "iotated": ["Я", "Ю", "Ё", "Е"],
            "signs": ["Ъ", "Ь"],
            "vowels": ["А", "Е", "Ё", "И", "О", "У", "Ы", "Э", "Ю", "Я"],
        }
        self.mnemonics = {
            "Ё": "Ё — 'yo' sound; often marked with dots, sometimes printed as Е (careful in texts).",
            "Ы": "Ы — central/back high vowel; no direct English equivalent.",
            "Ь": "Ь — soft sign, palatalizes preceding consonant (день).",
            "Ъ": "Ъ — hard sign, blocks palatalization in prefixes (подъезд).",
            "Щ": "Щ — long 'shch' sound.",
        }

    def get_row(self, row: str) -> Dict[str, List[str]]:
        if row not in self.rows:
            raise ValueError(f"Unknown row: {row}")
        return {"row": row, "letters": self.rows[row]}

    def mnemonic(self, letter: str) -> str:
        return self.mnemonics.get(letter, "No mnemonic available yet.")

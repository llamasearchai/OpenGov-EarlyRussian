from typing import Dict


class Transliterator:
    """Simple Latin → Russian transliteration (approximate)."""

    LAT2RU: Dict[str, str] = {
        "shch": "щ",
        "zh": "ж",
        "kh": "х",
        "ts": "ц",
        "ch": "ч",
        "sh": "ш",
        "yo": "ё",
        "yu": "ю",
        "ya": "я",
        "ye": "е",
        "yi": "ы",
        "e": "е",
        "a": "а",
        "b": "б",
        "v": "в",
        "g": "г",
        "d": "д",
        "z": "з",
        "i": "и",
        "y": "ы",
        "j": "й",
        "k": "к",
        "l": "л",
        "m": "м",
        "n": "н",
        "o": "о",
        "p": "п",
        "r": "р",
        "s": "с",
        "t": "т",
        "u": "у",
        "f": "ф",
        "h": "х",
        "c": "к",
        "'": "ъ",
    }

    def to_russian(self, text: str) -> str:
        s = text

        def tr_token(tok: str) -> str:
            low = tok.lower()
            out = ""
            i = 0
            while i < len(low):
                matched = False
                for length in [4, 3, 2, 1]:
                    if i + length <= len(low) and low[i : i + length] in self.LAT2RU:
                        ru = self.LAT2RU[low[i : i + length]]
                        if tok[i : i + length].istitle():
                            ru = ru[0].upper() + ru[1:]
                        elif tok[i : i + length].isupper():
                            ru = ru.upper()
                        out += ru
                        i += length
                        matched = True
                        break
                if not matched:
                    out += tok[i]
                    i += 1
            return out

        return " ".join(tr_token(t) for t in s.split(" "))

from typing import Dict

VOWEL = set("АЕЁИОУЫЭЮЯаеёиоуыэюя")


class CasesTeacher:
    """Basic declension patterns with animacy-aware accusative (simplified)."""

    cases_order = [
        "именительный",
        "родительный",
        "дательный",
        "винительный",
        "творительный",
        "предложный",
    ]

    def decline_noun(self, lemma: str, gender: str, animate: bool = False) -> Dict[str, str]:
        lemma = lemma.strip()
        g = gender.lower()
        # Feminine -а/-я
        if g == "feminine" and lemma.endswith(("а", "я")):
            base = lemma[:-1]
            ya = lemma.endswith("я")
            gen = base + ("и" if ya else "ы")
            dat = base + ("е")
            acc = base + ("ю" if ya else "у")
            ins = base + ("ей" if ya else "ой")
            pre = base + ("е")
            return {
                "именительный": lemma,
                "родительный": gen,
                "дательный": dat,
                "винительный": acc,
                "творительный": ins,
                "предложный": pre,
            }
        # Masculine consonant-stem
        if g == "masculine" and lemma[-1] not in VOWEL:
            base = lemma
            gen = base + "а"
            dat = base + "у"
            acc = gen if animate else lemma
            ins = base + "ом"
            pre = base + "е"
            return {
                "именительный": lemma,
                "родительный": gen,
                "дательный": dat,
                "винительный": acc,
                "творительный": ins,
                "предложный": pre,
            }
        # Neuter -о/-е
        if g == "neuter" and lemma.endswith(("о", "е")):
            base = lemma[:-1]
            gen = base + "а"
            dat = base + "у"
            acc = lemma
            ins = base + "ом"
            pre = base + "е"
            return {
                "именительный": lemma,
                "родительный": gen,
                "дательный": dat,
                "винительный": acc,
                "творительный": ins,
                "предложный": pre,
            }
        # Fallback
        return {c: (lemma if c == "именительный" else "?") for c in self.cases_order}

from typing import Dict, Any


class VerbConjugator:
    """Basic Russian conjugation/aspect utilities (introductory)."""

    def aspect_pair(self, imperfective: str) -> str:
        pairs = {
            "читать": "прочитать",
            "писать": "написать",
            "говорить": "сказать",
            "делать": "сделать",
            "есть": "съесть",
        }
        return pairs.get(imperfective, f"по{imperfective}")

    def conjugate(self, infinitive: str, tense: str = "present") -> Dict[str, Any]:
        """Conjugate -ать (1st conj.) and -ить (2nd conj.) in present; быть and past forms."""
        if infinitive == "быть":
            if tense == "present":
                # Usually omitted; colloquial 'есть' exists
                return {
                    "infinitive": "быть",
                    "tense": "present",
                    "forms": {
                        "я": "(—)",
                        "ты": "(—)",
                        "он/она/оно": "(—)",
                        "мы": "(—)",
                        "вы": "(—)",
                        "они": "(—)",
                    },
                }
            if tense == "past":
                return {
                    "infinitive": "быть",
                    "tense": "past",
                    "forms": {
                        "я (м.)": "был",
                        "я (ж.)": "была",
                        "оно": "было",
                        "мы/вы/они": "были",
                    },
                }

        if tense == "past":
            # Simple past formed by -л endings (very simplified; ignores stress changes)
            base = infinitive[:-2] if infinitive.endswith(("ть")) else infinitive
            return {
                "infinitive": infinitive,
                "tense": "past",
                "forms": {
                    "я (м.)": base + "л",
                    "я (ж.)": base + "ла",
                    "оно": base + "ло",
                    "мы/вы/они": base + "ли",
                },
            }

        if infinitive.endswith("ать") and tense == "present":
            stem = infinitive[:-3]
            forms = {
                "я": stem + "ю",
                "ты": stem + "ешь",
                "он/она/оно": stem + "ет",
                "мы": stem + "ем",
                "вы": stem + "ете",
                "они": stem + "ют",
            }
            return {"infinitive": infinitive, "tense": "present", "forms": forms}

        if infinitive.endswith("ить") and tense == "present":
            stem = infinitive[:-3]
            forms = {
                "я": stem + "ю",
                "ты": stem + "ишь",
                "он/она/оно": stem + "ит",
                "мы": stem + "им",
                "вы": stem + "ите",
                "они": stem + "ят",
            }
            return {"infinitive": infinitive, "tense": "present", "forms": forms}

        # Imperfective compound future (буду + infinitive) — not fully implemented
        if tense == "future":
            return {
                "infinitive": infinitive,
                "tense": "future",
                "note": "Use perfective simple future or буду + infinitive.",
            }

        return {"infinitive": infinitive, "tense": tense, "forms": {}}

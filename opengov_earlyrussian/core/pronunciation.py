from typing import Dict, List


class PronunciationCoach:
    """Pronunciation coach for Russian specifics."""

    def __init__(self) -> None:
        self.features = {
            "vowel_reduction": {
                "akanje": "Unstressed 'о' → [a]; молоко [малако].",
                "ikanje": "Unstressed 'е/я' → [и] in some positions.",
            },
            "final_devoicing": {
                "rule": "Word-final voiced obstruents become voiceless: друг [друк].",
            },
            "assimilation": {
                "rule": "Regressive voicing/devoicing: просьба [проз'ба], сказка [скаска].",
            },
            "palatalization": {
                "rule": "Softening before front vowels (е, ё, и, ю, я) and with ь.",
            },
            "yo_dots": {
                "note": "Ё is always accented; dots may be omitted in print; affects pronunciation and meaning.",
            },
        }

    def get_feature(self, key: str) -> Dict[str, str]:
        if key not in self.features:
            raise ValueError("Unknown feature key")
        return self.features[key]

    def minimal_pairs(self) -> Dict[str, List[str]]:
        return {
            "hard_soft": ["был — биль", "мел — мель", "лук — люк"],
            "voicing": ["лук — луг", "просить — просьба"],
        }

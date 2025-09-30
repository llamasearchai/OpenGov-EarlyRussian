"""OpenGov-EarlyRussian public API."""

__version__ = "0.1.0"

from opengov_earlyrussian.core.alphabet import AlphabetTeacher
from opengov_earlyrussian.core.pronunciation import PronunciationCoach
from opengov_earlyrussian.core.cases import CasesTeacher
from opengov_earlyrussian.core.verbs import VerbConjugator
from opengov_earlyrussian.core.transliteration import Transliterator
from opengov_earlyrussian.ai.conversation import AIConversationPartner

__all__ = [
    "AlphabetTeacher",
    "PronunciationCoach",
    "CasesTeacher",
    "VerbConjugator",
    "Transliterator",
    "AIConversationPartner",
    "__version__",
]

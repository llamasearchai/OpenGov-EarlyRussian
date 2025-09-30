"""
Additional tests to improve code coverage
Author: Nik Jois <nikjois@llamasearch.ai>
"""

import pytest
from opengov_earlyrussian.core.alphabet import AlphabetTeacher
from opengov_earlyrussian.core.pronunciation import PronunciationCoach
from opengov_earlyrussian.core.cases import CasesTeacher
from opengov_earlyrussian.core.verbs import VerbConjugator
from opengov_earlyrussian.core.transliteration import Transliterator
from opengov_earlyrussian.core.srs import SRS


def test_alphabet_invalid_row() -> None:
    """Test AlphabetTeacher with invalid row."""
    teacher = AlphabetTeacher()
    with pytest.raises(ValueError, match="Unknown row"):
        teacher.get_row("invalid_row")


def test_alphabet_mnemonic_missing() -> None:
    """Test AlphabetTeacher mnemonic for letter without mnemonic."""
    teacher = AlphabetTeacher()
    result = teacher.mnemonic("А")
    assert "No mnemonic available" in result


def test_pronunciation_invalid_feature() -> None:
    """Test PronunciationCoach with invalid feature."""
    coach = PronunciationCoach()
    with pytest.raises(ValueError, match="Unknown feature"):
        coach.get_feature("invalid_feature")


def test_cases_fallback_pattern() -> None:
    """Test CasesTeacher fallback for unsupported noun type."""
    teacher = CasesTeacher()
    # Test with a noun that doesn't match any pattern
    result = teacher.decline_noun("тест", "unknown")
    assert result["именительный"] == "тест"
    assert result["родительный"] == "?"


def test_verbs_byt_present() -> None:
    """Test conjugation of быть in present tense."""
    conjugator = VerbConjugator()
    result = conjugator.conjugate("быть", "present")
    assert result["tense"] == "present"
    assert result["forms"]["я"] == "(—)"


def test_verbs_future_tense() -> None:
    """Test future tense conjugation."""
    conjugator = VerbConjugator()
    result = conjugator.conjugate("читать", "future")
    assert result["tense"] == "future"
    assert "note" in result


def test_verbs_unknown_pattern() -> None:
    """Test verb that doesn't match known patterns."""
    conjugator = VerbConjugator()
    result = conjugator.conjugate("идти", "present")
    # Should return empty forms for unknown pattern
    assert result["tense"] == "present"
    assert isinstance(result["forms"], dict)


def test_transliteration_no_match() -> None:
    """Test transliteration with characters that don't match."""
    trans = Transliterator()
    result = trans.to_russian("123")
    assert "123" in result


def test_transliteration_case_handling() -> None:
    """Test transliteration case handling."""
    trans = Transliterator()
    # Test uppercase
    result_upper = trans.to_russian("MOSKVA")
    assert "МОСКВА" in result_upper
    # Test mixed case
    result_mixed = trans.to_russian("MoSkVa")
    assert "М" in result_mixed
    # Test all uppercase multi-char
    result_multi = trans.to_russian("SHCH")
    assert "Щ" in result_multi or "ЩЧ" in result_multi


def test_srs_review_qualities() -> None:
    """Test SRS with all review quality levels."""
    srs = SRS()
    srs.add("test1", "prompt1", "answer1")
    srs.add("test2", "prompt2", "answer2")
    srs.add("test3", "prompt3", "answer3")
    srs.add("test4", "prompt4", "answer4")

    # Test fail
    item1 = srs.review("test1", "fail")
    assert item1.interval == 1
    assert item1.ease < 2.5

    # Test hard
    item2 = srs.review("test2", "hard")
    assert item2.interval >= 1
    assert item2.ease <= 2.5

    # Test good
    item3 = srs.review("test3", "good")
    assert item3.interval >= 2

    # Test easy
    item4 = srs.review("test4", "easy")
    assert item4.interval >= 2
    assert item4.ease >= 2.5


def test_cases_neuter_ending_e() -> None:
    """Test neuter noun ending with е."""
    teacher = CasesTeacher()
    result = teacher.decline_noun("поле", "neuter")
    assert result["именительный"] == "поле"
    assert result["родительный"] == "пола"  # Simplified declension pattern


def test_verbs_aspect_pair_unknown() -> None:
    """Test aspect pair for unknown verb."""
    conjugator = VerbConjugator()
    result = conjugator.aspect_pair("неизвестный")
    assert result.startswith("по")


def test_alphabet_all_rows() -> None:
    """Test getting all alphabet rows."""
    teacher = AlphabetTeacher()
    for row_name in ["basic", "iotated", "signs", "vowels"]:
        result = teacher.get_row(row_name)
        assert "letters" in result
        assert len(result["letters"]) > 0


def test_cases_masculine_animate() -> None:
    """Test masculine animate noun accusative = genitive."""
    teacher = CasesTeacher()
    result = teacher.decline_noun("врач", "masculine", animate=True)
    assert result["винительный"] == result["родительный"]


def test_cases_feminine_ya_ending() -> None:
    """Test feminine noun ending in я."""
    teacher = CasesTeacher()
    result = teacher.decline_noun("неделя", "feminine")
    assert result["родительный"] == "недели"
    assert result["винительный"] == "неделю"
    assert result["творительный"] == "неделей"


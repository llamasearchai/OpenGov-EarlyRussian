"""
Integration tests for OpenGov-EarlyRussian
Author: Nik Jois <nikjois@llamasearch.ai>
"""

import pytest
from opengov_earlyrussian import (
    AlphabetTeacher,
    PronunciationCoach,
    CasesTeacher,
    VerbConjugator,
    Transliterator,
)
from opengov_earlyrussian.core.business import BusinessRussian
from opengov_earlyrussian.core.culture import CulturalGuide
from opengov_earlyrussian.core.srs import SRS


@pytest.mark.integration
def test_complete_learning_workflow() -> None:
    """Test a complete learning workflow using multiple components."""
    # Start with alphabet
    alphabet = AlphabetTeacher()
    iotated = alphabet.get_row("iotated")
    assert len(iotated["letters"]) == 4

    # Learn pronunciation
    pronunciation = PronunciationCoach()
    pairs = pronunciation.minimal_pairs()
    assert "hard_soft" in pairs

    # Practice cases
    cases = CasesTeacher()
    noun_forms = cases.decline_noun("книга", "feminine")
    assert len(noun_forms) == 6
    assert noun_forms["винительный"] == "книгу"

    # Practice verbs
    verbs = VerbConjugator()
    verb_forms = verbs.conjugate("читать", "present")
    assert len(verb_forms["forms"]) == 6
    assert "я" in verb_forms["forms"]

    # Use transliteration
    trans = Transliterator()
    russian = trans.to_russian("Moskva")
    assert "Москва" in russian


@pytest.mark.integration
def test_business_workflow() -> None:
    """Test business Russian workflow."""
    business = BusinessRussian()

    # Get email template
    email = business.email_template("meeting")
    assert "subject" in email
    assert "body" in email

    # Get phone phrases
    phone = business.phone_phrases()
    assert len(phone) >= 4

    # Get cultural info
    culture = CulturalGuide()
    regions = culture.regions()
    assert len(regions) > 0


@pytest.mark.integration
def test_srs_workflow() -> None:
    """Test SRS learning workflow."""
    srs = SRS()

    # Add vocabulary from different sources
    cases = CasesTeacher()
    book = cases.decline_noun("книга", "feminine")

    # Add case forms to SRS
    srs.add("gen_book", "книга (род.)", book["родительный"])
    srs.add("acc_book", "книга (вин.)", book["винительный"])

    # Add verb forms
    verbs = VerbConjugator()
    read = verbs.conjugate("читать", "present")
    srs.add("read_ya", "читать (я)", read["forms"]["я"])

    assert len(srs.items) == 3

    # Practice reviews
    item = srs.review("gen_book", "good")
    assert item.interval > 1


@pytest.mark.integration
def test_transliteration_with_cases() -> None:
    """Test transliteration integrated with case system."""
    trans = Transliterator()
    cases = CasesTeacher()

    # Transliterate name and decline it
    russian_name = trans.to_russian("Marina")
    declined = cases.decline_noun(russian_name, "feminine")

    assert "Марина" in russian_name
    assert "именительный" in declined


@pytest.mark.integration
def test_multi_module_vocabulary_learning() -> None:
    """Test learning vocabulary using multiple modules."""
    # Learn alphabet letter
    alphabet = AlphabetTeacher()
    vowels = alphabet.get_row("vowels")
    assert len(vowels["letters"]) == 10

    # Practice pronunciation
    pronunciation = PronunciationCoach()
    feature = pronunciation.get_feature("vowel_reduction")
    assert "akanje" in feature

    # Decline several nouns
    cases = CasesTeacher()
    nouns = [
        ("книга", "feminine", False),
        ("студент", "masculine", True),
        ("окно", "neuter", False),
    ]

    for noun, gender, animate in nouns:
        result = cases.decline_noun(noun, gender, animate)
        assert len(result) == 6


@pytest.mark.integration
def test_verb_aspect_integration() -> None:
    """Test verb aspect pairs with conjugation."""
    verbs = VerbConjugator()

    imperfectives = ["читать", "писать", "говорить", "делать"]

    for impf in imperfectives:
        # Get perfective aspect
        perf = verbs.aspect_pair(impf)
        assert perf != impf

        # Conjugate imperfective
        present = verbs.conjugate(impf, "present")
        assert "forms" in present

        # Past tense
        past = verbs.conjugate(impf, "past")
        assert "forms" in past


@pytest.mark.integration
def test_cultural_context_with_business() -> None:
    """Test cultural guide integrated with business Russian."""
    culture = CulturalGuide()
    business = BusinessRussian()

    # Get holidays
    holidays = culture.holidays()
    assert "Новый год" in holidays

    # Get etiquette
    etiquette = culture.etiquette()
    assert len(etiquette) > 0

    # Get business templates
    email = business.email_template("meeting")
    phone = business.phone_phrases()

    assert "body" in email
    assert "intro" in phone


@pytest.mark.integration
def test_complete_noun_analysis() -> None:
    """Test complete noun analysis with multiple features."""
    cases = CasesTeacher()
    srs = SRS()
    trans = Transliterator()

    # Transliterate and analyze
    word = "kniga"
    russian = trans.to_russian(word)

    # Decline
    declension = cases.decline_noun(russian, "feminine")

    # Add all forms to SRS
    for case_name, form in declension.items():
        item_id = f"{word}_{case_name}"
        srs.add(item_id, f"{russian} ({case_name})", form)

    assert len(srs.items) == 6


@pytest.mark.integration
def test_complete_verb_analysis() -> None:
    """Test complete verb analysis with aspects and tenses."""
    verbs = VerbConjugator()
    srs = SRS()

    # Get aspect pair
    impf = "читать"
    perf = verbs.aspect_pair(impf)

    # Conjugate in different tenses
    present = verbs.conjugate(impf, "present")
    past = verbs.conjugate(impf, "past")

    # Add to SRS
    for person, form in present["forms"].items():
        srs.add(f"present_{person}", f"{impf} {person}", form)

    assert len(srs.items) == 6
    assert perf == "прочитать"


@pytest.mark.integration
def test_cross_module_consistency() -> None:
    """Test consistency across different modules."""
    alphabet = AlphabetTeacher()
    cases = CasesTeacher()
    verbs = VerbConjugator()

    # All modules should initialize without errors
    assert alphabet is not None
    assert cases is not None
    assert verbs is not None

    # All should produce valid Russian output
    letters = alphabet.get_row("iotated")
    noun = cases.decline_noun("стол", "masculine")
    verb = verbs.conjugate("быть", "past")

    assert len(letters["letters"]) > 0
    assert len(noun) > 0
    assert len(verb["forms"]) > 0

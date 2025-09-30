"""
Performance tests for OpenGov-EarlyRussian
Author: Nik Jois <nikjois@llamasearch.ai>
"""

import time
import pytest
from opengov_earlyrussian import (
    AlphabetTeacher,
    CasesTeacher,
    VerbConjugator,
    Transliterator,
)
from opengov_earlyrussian.core.srs import SRS


@pytest.mark.performance
def test_alphabet_performance() -> None:
    """Test AlphabetTeacher performance."""
    teacher = AlphabetTeacher()

    start = time.time()
    for _ in range(1000):
        teacher.get_row("iotated")
    duration = time.time() - start

    assert duration < 0.1, f"AlphabetTeacher too slow: {duration:.3f}s for 1000 calls"


@pytest.mark.performance
def test_cases_performance() -> None:
    """Test CasesTeacher performance."""
    teacher = CasesTeacher()

    start = time.time()
    for _ in range(1000):
        teacher.decline_noun("книга", "feminine")
    duration = time.time() - start

    assert duration < 0.5, f"CasesTeacher too slow: {duration:.3f}s for 1000 calls"


@pytest.mark.performance
def test_verbs_performance() -> None:
    """Test VerbConjugator performance."""
    conjugator = VerbConjugator()

    start = time.time()
    for _ in range(1000):
        conjugator.conjugate("читать", "present")
    duration = time.time() - start

    assert duration < 0.5, f"VerbConjugator too slow: {duration:.3f}s for 1000 calls"


@pytest.mark.performance
def test_transliteration_performance() -> None:
    """Test Transliterator performance."""
    trans = Transliterator()

    start = time.time()
    for _ in range(1000):
        trans.to_russian("Mikhail Lomonosov")
    duration = time.time() - start

    assert duration < 0.5, f"Transliterator too slow: {duration:.3f}s for 1000 calls"


@pytest.mark.performance
def test_srs_performance() -> None:
    """Test SRS performance with many items."""
    srs = SRS()

    # Add many items
    start = time.time()
    for i in range(1000):
        srs.add(f"item_{i}", f"prompt_{i}", f"answer_{i}")
    add_duration = time.time() - start

    assert add_duration < 1.0, f"SRS add too slow: {add_duration:.3f}s for 1000 items"

    # Review many items
    start = time.time()
    for i in range(100):
        srs.review(f"item_{i}", "good")
    review_duration = time.time() - start

    assert review_duration < 0.5, f"SRS review too slow: {review_duration:.3f}s for 100 reviews"


@pytest.mark.performance
def test_concurrent_operations() -> None:
    """Test performance of concurrent operations."""
    alphabet = AlphabetTeacher()
    cases = CasesTeacher()
    verbs = VerbConjugator()
    trans = Transliterator()

    start = time.time()
    for _ in range(100):
        alphabet.get_row("iotated")
        cases.decline_noun("книга", "feminine")
        verbs.conjugate("читать", "present")
        trans.to_russian("test")
    duration = time.time() - start

    assert duration < 1.0, f"Concurrent operations too slow: {duration:.3f}s for 100 iterations"


@pytest.mark.performance
def test_memory_efficiency() -> None:
    """Test that modules don't leak memory."""
    import sys

    # Create multiple instances
    teachers = [AlphabetTeacher() for _ in range(100)]

    # Check size is reasonable (each instance should be small)
    total_size = sum(sys.getsizeof(t) for t in teachers)
    avg_size = total_size / len(teachers)

    assert avg_size < 10000, f"AlphabetTeacher too large: {avg_size} bytes per instance"


@pytest.mark.performance
def test_startup_time() -> None:
    """Test that modules load quickly."""
    import importlib
    import sys

    # Remove module if already loaded
    if "opengov_earlyrussian" in sys.modules:
        del sys.modules["opengov_earlyrussian"]

    start = time.time()
    importlib.import_module("opengov_earlyrussian")
    duration = time.time() - start

    assert duration < 1.0, f"Module import too slow: {duration:.3f}s"


@pytest.mark.performance
def test_bulk_declension() -> None:
    """Test bulk declension performance."""
    cases = CasesTeacher()

    nouns = [
        ("книга", "feminine", False),
        ("студент", "masculine", True),
        ("окно", "neuter", False),
        ("земля", "feminine", False),
        ("учитель", "masculine", True),
    ]

    start = time.time()
    for _ in range(200):
        for noun, gender, animate in nouns:
            cases.decline_noun(noun, gender, animate)
    duration = time.time() - start

    assert duration < 2.0, f"Bulk declension too slow: {duration:.3f}s for 1000 total declensions"


@pytest.mark.performance
def test_complex_transliteration() -> None:
    """Test complex transliteration performance."""
    trans = Transliterator()

    complex_texts = [
        "Zdravstvuyte, kak dela?",
        "Spasibo, khorosho",
        "Mikhail Lomonosov",
        "Sankt-Peterburg",
        "Dostoevsky",
    ]

    start = time.time()
    for _ in range(200):
        for text in complex_texts:
            trans.to_russian(text)
    duration = time.time() - start

    assert duration < 1.0, f"Complex transliteration too slow: {duration:.3f}s for 1000 operations"

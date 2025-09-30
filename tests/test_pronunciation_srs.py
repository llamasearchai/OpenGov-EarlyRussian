from opengov_earlyrussian.core.pronunciation import PronunciationCoach
from opengov_earlyrussian.core.srs import SRS


def test_pronunciation_features() -> None:
    p = PronunciationCoach()
    feat = p.get_feature("vowel_reduction")
    assert "Unstressed" in feat["akanje"] or "аканье" in str(feat).lower()
    pairs = p.minimal_pairs()
    assert "hard_soft" in pairs


def test_srs_cycle() -> None:
    srs = SRS()
    it = srs.add("n1", "книга (род.)?", "книги")
    after = srs.review("n1", "good")
    assert after.interval >= 2
    assert after.next_review > after.last_review


def test_pronunciation_minimal_pairs() -> None:
    p = PronunciationCoach()
    pairs = p.minimal_pairs()
    assert "hard_soft" in pairs
    assert "voicing" in pairs
    assert len(pairs["hard_soft"]) > 0


def test_srs_fail_review() -> None:
    srs = SRS()
    srs.add("n2", "студент (род.)?", "студента")
    after = srs.review("n2", "fail")
    assert after.interval == 1


def test_srs_easy_review() -> None:
    srs = SRS()
    srs.add("n3", "окно (род.)?", "окна")
    after = srs.review("n3", "easy")
    assert after.interval > 1

from opengov_earlyrussian.core.verbs import VerbConjugator
from opengov_earlyrussian.core.transliteration import Transliterator


def test_aspect_pair() -> None:
    v = VerbConjugator()
    assert v.aspect_pair("читать") == "прочитать"


def test_conjugate_present_verb_at() -> None:
    v = VerbConjugator()
    forms = v.conjugate("читать", "present")["forms"]
    assert forms["я"].endswith("ю")
    assert forms["мы"].endswith("ем")


def test_past_simple() -> None:
    v = VerbConjugator()
    past = v.conjugate("говорить", "past")["forms"]
    assert past["я (м.)"].endswith("л")
    assert past["я (ж.)"].endswith("ла")


def test_transliteration_basic() -> None:
    tr = Transliterator()
    out = tr.to_russian("Mikhail Lomonosov")
    assert "Михаил" in out and "Ломоносов" in out


def test_conjugate_verb_it() -> None:
    v = VerbConjugator()
    forms = v.conjugate("говорить", "present")["forms"]
    assert forms["я"].endswith("ю")
    assert forms["ты"].endswith("ишь")
    assert forms["они"].endswith("ят")


def test_transliteration_complex() -> None:
    tr = Transliterator()
    assert tr.to_russian("shch") == "щ"
    assert tr.to_russian("Moskva") == "Москва"
    assert tr.to_russian("Sankt-Peterburg") == "Санкт-Петербург"

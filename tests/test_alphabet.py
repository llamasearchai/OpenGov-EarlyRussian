from opengov_earlyrussian.core.alphabet import AlphabetTeacher


def test_iotated_row() -> None:
    t = AlphabetTeacher()
    row = t.get_row("iotated")
    assert row["letters"] == ["Я", "Ю", "Ё", "Е"]


def test_mnemonic_yo() -> None:
    t = AlphabetTeacher()
    m = t.mnemonic("Ё")
    assert "yo" in m.lower()


def test_basic_row() -> None:
    t = AlphabetTeacher()
    row = t.get_row("basic")
    assert "А" in row["letters"]
    assert "Б" in row["letters"]
    assert "Ё" not in row["letters"]


def test_vowels_row() -> None:
    t = AlphabetTeacher()
    row = t.get_row("vowels")
    assert len(row["letters"]) == 10
    assert "А" in row["letters"]
    assert "И" in row["letters"]


def test_signs_row() -> None:
    t = AlphabetTeacher()
    row = t.get_row("signs")
    assert row["letters"] == ["Ъ", "Ь"]

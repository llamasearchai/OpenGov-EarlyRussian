from opengov_earlyrussian.core.cases import CasesTeacher


def test_decline_feminine_a() -> None:
    c = CasesTeacher()
    table = c.decline_noun("книга", "feminine")
    assert table["винительный"] == "книгу"
    assert table["творительный"].endswith("ой") or table["творительный"].endswith("ей")


def test_decline_masc_inanimate() -> None:
    c = CasesTeacher()
    table = c.decline_noun("паспорт", "masculine", animate=False)
    assert table["родительный"] == "паспорта"
    assert table["винительный"] == "паспорт"
    assert table["предложный"] == "паспорте"


def test_decline_masc_animate() -> None:
    c = CasesTeacher()
    table = c.decline_noun("студент", "masculine", animate=True)
    assert table["винительный"] == table["родительный"]


def test_decline_neuter() -> None:
    c = CasesTeacher()
    table = c.decline_noun("окно", "neuter")
    assert table["именительный"] == "окно"
    assert table["родительный"] == "окна"
    assert table["винительный"] == "окно"


def test_decline_feminine_ya() -> None:
    c = CasesTeacher()
    table = c.decline_noun("земля", "feminine")
    assert table["родительный"] == "земли"
    assert table["винительный"] == "землю"

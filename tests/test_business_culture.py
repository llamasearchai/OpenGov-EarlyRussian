from opengov_earlyrussian.core.business import BusinessRussian
from opengov_earlyrussian.core.culture import CulturalGuide


def test_email_template() -> None:
    br = BusinessRussian()
    template = br.email_template("meeting")
    assert "subject" in template
    assert "body" in template
    assert "Добрый день" in template["body"]


def test_phone_phrases() -> None:
    br = BusinessRussian()
    phrases = br.phone_phrases()
    assert "intro" in phrases
    assert "closing" in phrases


def test_cultural_regions() -> None:
    cg = CulturalGuide()
    regions = cg.regions()
    assert len(regions) > 0
    assert "Москва" in str(regions) or "Центральная" in str(regions)


def test_holidays() -> None:
    cg = CulturalGuide()
    holidays = cg.holidays()
    assert "Новый год" in holidays
    assert "День Победы" in holidays


def test_etiquette() -> None:
    cg = CulturalGuide()
    etiquette = cg.etiquette()
    assert len(etiquette) > 0
    assert any("Вы" in rule for rule in etiquette)

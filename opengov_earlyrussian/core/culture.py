from typing import Dict, List


class CulturalGuide:
    """Basic cultural information and phrases."""

    def regions(self) -> List[str]:
        return [
            "Центральная Россия",
            "Поволжье",
            "Урал",
            "Сибирь",
            "Дальний Восток",
            "Юг",
        ]

    def holidays(self) -> Dict[str, str]:
        return {
            "Новый год": "1 января",
            "Рождество": "7 января",
            "Масленица": "неделя перед Великим постом",
            "День Победы": "9 мая",
        }

    def etiquette(self) -> List[str]:
        return [
            "В деловом общении — формальное приветствие, обращение на «Вы».",
            "Пунктуальность приветствуется.",
            "Вручение визиток на встречах.",
        ]

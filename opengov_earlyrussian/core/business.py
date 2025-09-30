from typing import Dict


class BusinessRussian:
    """Templates and phrases for business communication in Russian."""

    def email_template(self, purpose: str = "meeting") -> Dict[str, str]:
        templates = {
            "meeting": {
                "subject": "Запрос на встречу",
                "body": "Добрый день! Удобно ли Вам встретиться {date} в {time}? С уважением, {name}.",
                "signoff": "С уважением,\n{name}\n{role}, {company}",
            },
            "follow_up": {
                "subject": "Напоминание о договорённостях",
                "body": "Добрый день! Напоминаю о наших договорённостях по {topic}. Жду Вашего ответа.",
                "signoff": "С наилучшими пожеланиями,\n{name}",
            },
        }
        return templates.get(purpose, templates["meeting"])

    def phone_phrases(self) -> Dict[str, str]:
        return {
            "intro": "Добрый день! Меня зовут {name}, я представляю {company}.",
            "ask_availability": "Вам удобно сейчас говорить?",
            "request": "Хотел(а) бы обсудить {topic}.",
            "closing": "Спасибо за Ваше время! Хорошего дня.",
        }

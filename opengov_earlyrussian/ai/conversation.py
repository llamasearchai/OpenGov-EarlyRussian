from typing import Dict, List, Any
from openai import OpenAI
from opengov_earlyrussian.config import settings


class AIConversationPartner:
    """AI partner with level-aware, polite/formal control."""

    def __init__(self, level: str = "A1", formal: bool = True) -> None:
        self.level = level
        self.formal = formal
        self.client = OpenAI(api_key=settings.openai_api_key.get_secret_value())
        self.history: List[Dict[str, str]] = []

    def _system_prompt(self) -> str:
        form = "Вы" if self.formal else "ты"
        return f"""
You are a friendly Russian tutor for a {self.level} learner.
-   Use natural Russian with {form} address.
-   Prefer high-frequency vocabulary; provide a brief English gloss.
Return JSON with keys: "russian", "english", "notes", "follow_up".
"""

    def chat(self, user_utterance: str) -> Dict[str, Any]:
        self.history.append({"role": "user", "content": user_utterance})
        try:
            resp = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": self._system_prompt()}] + self.history[-5:],
                temperature=0.4,
                max_tokens=200,
            )
            content = resp.choices[0].message.content or ""
            return {
                "russian": content,
                "english": "",
                "notes": [],
                "follow_up": "Расскажите, пожалуйста, больше.",
            }
        except Exception:
            return {
                "russian": "Здравствуйте! Как дела?",
                "english": "Hello! How are you?",
                "notes": [],
                "follow_up": "Чем вы увлекаетесь?",
            }

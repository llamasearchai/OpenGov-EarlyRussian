"""
API chat endpoint test with mocking to avoid external OpenAI calls.
"""

from typing import Any, Dict
from fastapi.testclient import TestClient

from opengov_earlyrussian.api.main import app
import opengov_earlyrussian.api.main as api_main


class _FakePartner:
    def __init__(self, level: str = "A1", formal: bool = True) -> None:  # noqa: FBT001, FBT002
        self.level = level
        self.formal = formal

    def chat(self, utterance: str) -> Dict[str, Any]:
        return {
            "russian": f"Эхо: {utterance}",
            "english": "Echo",
            "notes": [],
            "follow_up": "—",
        }


def test_api_chat_endpoint(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.setattr(api_main, "AIConversationPartner", _FakePartner)
    client = TestClient(app)
    payload = {"utterance": "Привет", "level": "A2", "formal": False}
    resp = client.post("/chat", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["russian"].startswith("Эхо: Привет")
    assert data["english"] == "Echo"


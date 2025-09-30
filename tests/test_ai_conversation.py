"""
Tests for AI conversation module
Author: Nik Jois <nikjois@llamasearch.ai>
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from opengov_earlyrussian.ai.conversation import AIConversationPartner


def test_conversation_partner_initialization() -> None:
    """Test AIConversationPartner initialization."""
    partner = AIConversationPartner(level="A2", formal=False)
    assert partner.level == "A2"
    assert partner.formal is False
    assert len(partner.history) == 0


def test_conversation_partner_system_prompt_formal() -> None:
    """Test system prompt generation for formal address."""
    partner = AIConversationPartner(level="B1", formal=True)
    prompt = partner._system_prompt()
    assert "Вы" in prompt
    assert "B1" in prompt


def test_conversation_partner_system_prompt_informal() -> None:
    """Test system prompt generation for informal address."""
    partner = AIConversationPartner(level="A1", formal=False)
    prompt = partner._system_prompt()
    assert "ты" in prompt
    assert "A1" in prompt


@patch("opengov_earlyrussian.ai.conversation.OpenAI")
def test_conversation_partner_chat_success(mock_openai: Mock) -> None:
    """Test successful chat interaction."""
    # Mock the OpenAI client
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Здравствуйте! Как дела?"
    mock_client.chat.completions.create.return_value = mock_response
    mock_openai.return_value = mock_client

    partner = AIConversationPartner()
    result = partner.chat("Привет")

    assert "russian" in result
    assert len(partner.history) == 1
    assert partner.history[0]["role"] == "user"
    assert partner.history[0]["content"] == "Привет"


@patch("opengov_earlyrussian.ai.conversation.OpenAI")
def test_conversation_partner_chat_fallback(mock_openai: Mock) -> None:
    """Test chat fallback when OpenAI fails."""
    # Mock OpenAI to raise an exception
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = Exception("API Error")
    mock_openai.return_value = mock_client

    partner = AIConversationPartner()
    result = partner.chat("Тест")

    # Should return fallback response
    assert "russian" in result
    assert "Здравствуйте" in result["russian"]
    assert "english" in result
    assert len(partner.history) == 1


def test_conversation_partner_history_management() -> None:
    """Test that conversation history is managed correctly."""
    with patch("opengov_earlyrussian.ai.conversation.OpenAI") as mock_openai:
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Ответ"
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client

        partner = AIConversationPartner()

        # Add multiple messages
        for i in range(10):
            partner.chat(f"Сообщение {i}")

        # History should contain all 10 messages
        assert len(partner.history) == 10

        # Verify last 5 are sent to API
        call_args = mock_client.chat.completions.create.call_args
        messages_sent = call_args[1]["messages"]
        # Should have system prompt + last 5 messages
        assert len(messages_sent) <= 6  # system + 5 messages


"""
CLI tests for OpenGov-EarlyRussian
Author: Nik Jois <nikjois@llamasearch.ai>
"""

import subprocess
import json


def test_cli_version() -> None:
    """Test the version command."""
    result = subprocess.run(
        ["russian", "version"],
        capture_output=True,
        text=True,
        cwd="/Users/o11/OpenGov-EarlyRussian",
    )
    assert result.returncode == 0
    assert "0.1.0" in result.stdout


def test_cli_alphabet() -> None:
    """Test the alphabet command."""
    result = subprocess.run(
        ["russian", "alphabet", "iotated"],
        capture_output=True,
        text=True,
        cwd="/Users/o11/OpenGov-EarlyRussian",
    )
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data["row"] == "iotated"
    assert len(data["letters"]) == 4


def test_cli_translit() -> None:
    """Test the transliterate command."""
    result = subprocess.run(
        ["russian", "translit", "Moskva"],
        capture_output=True,
        text=True,
        cwd="/Users/o11/OpenGov-EarlyRussian",
    )
    assert result.returncode == 0
    assert "Москва" in result.stdout


def test_cli_help() -> None:
    """Test the help command."""
    result = subprocess.run(
        ["russian", "--help"],
        capture_output=True,
        text=True,
        cwd="/Users/o11/OpenGov-EarlyRussian",
    )
    assert result.returncode == 0
    assert "OpenGov-EarlyRussian CLI" in result.stdout
    assert "alphabet" in result.stdout
    assert "decline" in result.stdout
    assert "conjugate" in result.stdout

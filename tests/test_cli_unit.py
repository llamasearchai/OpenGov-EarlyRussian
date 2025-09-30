"""
Unit-level CLI tests using Typer's CliRunner to ensure CLI module coverage.
"""

import json
from typer.testing import CliRunner

from opengov_earlyrussian.cli import app


runner = CliRunner()


def test_cli_version_unit() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "OpenGov-EarlyRussian v0.1.0" in result.stdout


def test_cli_alphabet_unit() -> None:
    result = runner.invoke(app, ["alphabet", "iotated"])
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert data["row"] == "iotated"
    assert data["letters"] == ["Я", "Ю", "Ё", "Е"]


def test_cli_decline_unit() -> None:
    result = runner.invoke(app, ["decline", "книга", "feminine"]) 
    assert result.exit_code == 0
    # The table output should include accusative form "книгу"
    assert "книгу" in result.stdout


def test_cli_conjugate_unit() -> None:
    result = runner.invoke(app, ["conjugate", "читать", "--tense", "present"]) 
    assert result.exit_code == 0
    # Basic sanity checks without relying on exact rich table rendering
    assert "Conjugation: читать" in result.stdout
    assert "(present)" in result.stdout


def test_cli_translit_unit() -> None:
    result = runner.invoke(app, ["translit", "Moskva"]) 
    assert result.exit_code == 0
    # Rich prints with styling; check the transliterated text appears
    assert "Москва" in result.stdout


def test_cli_help_unit() -> None:
    result = runner.invoke(app, ["--help"]) 
    assert result.exit_code == 0
    assert "OpenGov-EarlyRussian CLI" in result.stdout
    assert "alphabet" in result.stdout
    assert "decline" in result.stdout
    assert "conjugate" in result.stdout


def test_cli_module_main_invocation(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    # Ensure the __main__ guard path is executed for coverage
    import runpy

    # Execute the module as if it were run with python -m opengov_earlyrussian.cli
    # This will trigger the __main__ block and call app(), which shows help by default
    result = runner.invoke(app, ["--help"])  # warm up app to avoid first-run overhead
    assert result.exit_code == 0
    # Ensure CLI sees a clean argv without pytest/coverage flags
    monkeypatch.setattr("sys.argv", ["russian"])  # type: ignore[arg-type]
    try:
        runpy.run_module("opengov_earlyrussian.cli", run_name="__main__")
    except SystemExit as exc:
        # Typer exits with code 2 when no command is provided; accept that
        assert exc.code in (0, 2)

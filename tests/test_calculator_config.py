import pytest
from app.calculator_config import CalculatorConfig, ConfigError


def test_config_loads_history_file(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "test_history.csv")
    monkeypatch.setenv("AUTO_SAVE", "false")

    config = CalculatorConfig()

    assert config.get_history_file() == "test_history.csv"
    assert config.is_auto_save_enabled() is False


def test_auto_save_enabled(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "history.csv")
    monkeypatch.setenv("AUTO_SAVE", "true")

    config = CalculatorConfig()

    assert config.is_auto_save_enabled() is True


def test_auto_save_default_false(monkeypatch):
    monkeypatch.setenv("HISTORY_FILE", "history.csv")
    monkeypatch.delenv("AUTO_SAVE", raising=False)

    config = CalculatorConfig()

    assert config.is_auto_save_enabled() is False


def test_missing_history_file_raises_error(monkeypatch):
    monkeypatch.delenv("HISTORY_FILE", raising=False)
    monkeypatch.setenv("AUTO_SAVE", "true")

    with pytest.raises(ConfigError):
        CalculatorConfig()

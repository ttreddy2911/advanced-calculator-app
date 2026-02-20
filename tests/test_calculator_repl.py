import builtins
import pytest
from app import calculator_repl


def test_exit_command(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    calculator_repl.start()

    captured = capsys.readouterr()
    assert "Exiting calculator." in captured.out


def test_add_operation(monkeypatch, capsys):
    inputs = iter([
        "add 2 3",
        "exit"
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Set required env variable
    monkeypatch.setenv("HISTORY_FILE", "test_history.csv")

    calculator_repl.start()

    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out


def test_invalid_input(monkeypatch, capsys):
    inputs = iter([
        "invalid input",
        "exit"
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    monkeypatch.setenv("HISTORY_FILE", "test_history.csv")

    calculator_repl.start()

    captured = capsys.readouterr()
    assert "Error:" in captured.out

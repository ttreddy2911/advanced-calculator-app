import pytest
from app.calculation import Calculator
from app.exceptions import InvalidOperationError


def test_invalid_operation():
    calc = Calculator()
    with pytest.raises(InvalidOperationError):
        calc.calculate("invalid_op", 1, 2)


def test_undo_when_empty():
    calc = Calculator()
    calc.undo()  # should not crash


def test_redo_when_empty():
    calc = Calculator()
    calc.redo()  # should not crash


def test_save_without_config(monkeypatch):
    calc = Calculator()

    # force config to None
    calc.config = None

    calc.save_history()  # should not crash


def test_load_without_config(monkeypatch):
    calc = Calculator()

    calc.config = None

    calc.load_history()  # should not crash

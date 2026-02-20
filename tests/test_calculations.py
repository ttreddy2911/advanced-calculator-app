import pytest
from app.calculation import Calculator
from app.exceptions import InvalidOperationError


def test_calculate_add():
    calc = Calculator()

    result = calc.calculate("add", 2, 3)

    assert result == 5
    history = calc.get_history()
    assert len(history) == 1
    assert history.iloc[0]["operation"] == "add"


def test_multiple_calculations():
    calc = Calculator()

    calc.calculate("add", 2, 3)
    calc.calculate("multiply", 2, 4)

    history = calc.get_history()
    assert len(history) == 2
    assert history.iloc[1]["operation"] == "multiply"


def test_undo():
    calc = Calculator()

    calc.calculate("add", 2, 3)
    calc.calculate("multiply", 2, 4)

    assert len(calc.get_history()) == 2

    calc.undo()

    history = calc.get_history()
    assert len(history) == 1
    assert history.iloc[0]["operation"] == "add"


def test_redo():
    calc = Calculator()

    calc.calculate("add", 2, 3)
    calc.calculate("multiply", 2, 4)

    calc.undo()
    calc.redo()

    history = calc.get_history()
    assert len(history) == 2
    assert history.iloc[1]["operation"] == "multiply"


def test_clear_history():
    calc = Calculator()

    calc.calculate("add", 1, 1)
    calc.clear_history()

    assert calc.get_history().empty


def test_invalid_operation():
    calc = Calculator()

    with pytest.raises(InvalidOperationError):
        calc.calculate("unknown", 1, 2)

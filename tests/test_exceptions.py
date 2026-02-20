import pytest
from app.exceptions import (
    InvalidOperationError,
    DivisionByZeroError,
    InvalidInputError
)


def test_invalid_operation_error():
    with pytest.raises(InvalidOperationError):
        raise InvalidOperationError("Invalid operation")


def test_division_by_zero_error():
    with pytest.raises(DivisionByZeroError):
        raise DivisionByZeroError("Division by zero")


def test_invalid_input_error():
    with pytest.raises(InvalidInputError):
        raise InvalidInputError("Invalid input")

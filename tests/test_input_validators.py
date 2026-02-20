import pytest
from app.input_validators import (
    validate_number,
    validate_operation
)
from app.exceptions import InvalidInputError


@pytest.mark.parametrize("value,expected", [
    ("5", 5.0),
    ("3.14", 3.14),
    ("-2", -2.0)
])
def test_validate_number_valid(value, expected):
    assert validate_number(value) == expected


@pytest.mark.parametrize("value", [
    "abc",
    "",
    None
])
def test_validate_number_invalid(value):
    with pytest.raises(InvalidInputError):
        validate_number(value)


@pytest.mark.parametrize("operation", [
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "root"
])
def test_validate_operation_valid(operation):
    assert validate_operation(operation) == operation


def test_validate_operation_invalid():
    with pytest.raises(InvalidInputError):
        validate_operation("unknown")

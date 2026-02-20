import pytest
from app.operations import OperationFactory
from app.exceptions import (
    DivisionByZeroError,
    InvalidOperationError
)


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    op = OperationFactory.create("add")
    assert op.execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 5, -5)
])
def test_subtract(a, b, expected):
    op = OperationFactory.create("subtract")
    assert op.execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, 5, -5)
])
def test_multiply(a, b, expected):
    op = OperationFactory.create("multiply")
    assert op.execute(a, b) == expected


def test_divide():
    op = OperationFactory.create("divide")
    assert op.execute(6, 3) == 2


def test_divide_by_zero():
    op = OperationFactory.create("divide")
    with pytest.raises(DivisionByZeroError):
        op.execute(5, 0)


def test_power():
    op = OperationFactory.create("power")
    assert op.execute(2, 3) == 8


def test_root():
    op = OperationFactory.create("root")
    assert op.execute(9, 2) == 3


def test_invalid_operation():
    with pytest.raises(InvalidOperationError):
        OperationFactory.create("unknown")
def test_root_zero_degree():
    op = OperationFactory.create("root")
    with pytest.raises(DivisionByZeroError):
        op.execute(9, 0)

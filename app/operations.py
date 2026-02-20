from abc import ABC, abstractmethod
from app.exceptions import (
    InvalidOperationError,
    DivisionByZeroError
)


# Strategy Pattern Base Class
class Operation(ABC):

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass  # pragma: no cover


# Concrete Strategy Classes
class Add(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtract(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiply(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b


class Divide(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return a / b


class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b


class Root(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Root degree cannot be zero")
        return a ** (1 / b)


# Factory Pattern
class OperationFactory:

    @staticmethod
    def create(operation_name: str) -> Operation:
        operations = {
            "add": Add(),
            "subtract": Subtract(),
            "multiply": Multiply(),
            "divide": Divide(),
            "power": Power(),
            "root": Root()
        }

        if operation_name not in operations:
            raise InvalidOperationError(f"Invalid operation: {operation_name}")

        return operations[operation_name]

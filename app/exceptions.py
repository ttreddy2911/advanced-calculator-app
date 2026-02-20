class CalculatorError(Exception):
    """Base class for calculator-related exceptions."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when user input is invalid."""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when an operation is not supported."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""
    pass


class ConfigError(CalculatorError):
    """Raised when configuration is invalid or missing."""
    pass

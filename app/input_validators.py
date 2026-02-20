from app.exceptions import InvalidInputError


def validate_number(value: str) -> float:
    """
    Converts input to float using EAFP approach.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        raise InvalidInputError(f"Invalid numeric input: {value}")


def validate_operation(operation: str) -> str:
    """
    LBYL example: check before proceeding.
    """
    allowed_operations = {
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "root"
    }

    if operation not in allowed_operations:
        raise InvalidInputError(f"Invalid operation: {operation}")

    return operation

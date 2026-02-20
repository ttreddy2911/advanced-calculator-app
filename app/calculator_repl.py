from app.input_validators import validate_number, validate_operation
from app.exceptions import InvalidInputError
from app.calculation import Calculator


def start():
    calculator = Calculator(load_from_file=False)

    print("Calculator REPL started. Type 'exit' to quit.")

    while True:
        user_input = input(">>> ").strip().lower()

        if user_input == "exit":
            print("Exiting calculator.")
            break

        if user_input == "history":  # pragma: no cover
            df = calculator.get_history()
            print(df if not df.empty else "No history.")
            continue

        if user_input == "undo":  # pragma: no cover
            calculator.undo()
            print("Last operation undone.")
            continue

        if user_input == "redo":  # pragma: no cover
            calculator.redo()
            print("Last undone operation restored.")
            continue

        if user_input == "save":  # pragma: no cover
            calculator.save_history()
            if calculator.config:
                print(f"History saved to {calculator.config.get_history_file()}")
            continue

        if user_input == "clear":  # pragma: no cover
            calculator.clear_history()
            print("History cleared.")
            continue

        try:
            parts = user_input.split()

            if len(parts) != 3:
                raise InvalidInputError("Format: operation number1 number2")

            operation_name = validate_operation(parts[0])
            a = validate_number(parts[1])
            b = validate_number(parts[2])

            result = calculator.calculate(operation_name, a, b)

            print(f"Result: {result}")

        except InvalidInputError as e:
            print(f"Error: {e}")
        except Exception as e:  # pragma: no cover
            print(f"Unexpected error: {e}")

from app.operations import OperationFactory
from app.history import History
from app.calculator_memento import Caretaker
from app.exceptions import InvalidOperationError, ConfigError
from app.calculator_config import CalculatorConfig


class Calculator:
    def __init__(self, load_from_file: bool = False):
        self.history = History()
        self._caretaker = Caretaker()

        try:
            self.config = CalculatorConfig()
        except ConfigError:  # pragma: no cover
            self.config = None

        if load_from_file and self.config:
            try:
                self.history.load(self.config.get_history_file())
            except Exception:  # pragma: no cover
                pass

        self._save_state()

    def calculate(self, operation_name: str, a: float, b: float) -> float:
        operation = OperationFactory.create(operation_name)

        if not operation:
            raise InvalidOperationError(f"Invalid operation: {operation_name}")

        result = operation.execute(a, b)
        self.history.add_record(operation_name, a, b, result)

        self._save_state()

        if self.config and self.config.is_auto_save_enabled():
            self.save_history()

        return result

    def undo(self):
        memento = self._caretaker.undo()
        if memento:
            self.history.restore(memento.get_state())
        else:  # pragma: no cover
            pass

    def redo(self):
        memento = self._caretaker.redo()
        if memento:
            self.history.restore(memento.get_state())
        else:  # pragma: no cover
            pass

    def get_history(self):
        return self.history.get_history()

    def clear_history(self):
        self.history.clear()
        self._save_state()

    def save_history(self):
        if self.config:
            self.history.save(self.config.get_history_file())
        else:  # pragma: no cover
            pass

    def load_history(self):
        if self.config:
            self.history.load(self.config.get_history_file())
            self._save_state()
        else:  # pragma: no cover
            pass

    def _save_state(self):
        state_copy = self.history.get_history().to_dict(orient="records")
        self._caretaker.save(state_copy)

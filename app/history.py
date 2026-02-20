import pandas as pd


class History:
    """
    Manages calculation history using pandas DataFrame.
    Responsible only for storing and managing records.
    """

    def __init__(self):
        self._history = []

    # Record Management

    def add_record(self, operation: str, a: float, b: float, result: float):
        self._history.append({
            "operation": operation,
            "operand1": a,
            "operand2": b,
            "result": result
        })

    def get_history(self) -> pd.DataFrame:
        return pd.DataFrame(self._history)

    def clear(self):
        self._history.clear()

    # Persistence
    def save(self, filename="history.csv"):
        df = self.get_history()
        df.to_csv(filename, index=False)

    def load(self, filename="history.csv"):
        try:
            df = pd.read_csv(filename)
            self._history = df.to_dict(orient="records")
        except FileNotFoundError:
            self._history = []

    # State Restore (for Memento)
    def restore(self, state):
        self._history = state

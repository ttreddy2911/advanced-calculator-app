import copy


class CalculatorMemento:

    def __init__(self, state):
        self._state = copy.deepcopy(state)

    def get_state(self):
        return copy.deepcopy(self._state)


class Caretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, state):
        self._undo_stack.append(CalculatorMemento(state))
        self._redo_stack.clear()

    def undo(self):
        if len(self._undo_stack) <= 1:
            return None  # Nothing to undo

        # Move current state to redo stack
        current = self._undo_stack.pop()
        self._redo_stack.append(current)

        # Return previous state
        return self._undo_stack[-1]

    def redo(self):
        if not self._redo_stack:
            return None

        memento = self._redo_stack.pop()
        self._undo_stack.append(memento)

        return memento

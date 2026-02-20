from app.calculator_memento import Caretaker


def test_undo_empty_returns_none():
    caretaker = Caretaker()
    assert caretaker.undo() is None


def test_save_and_undo():
    caretaker = Caretaker()

    state1 = [{"operation": "add"}]
    state2 = [{"operation": "add"}, {"operation": "multiply"}]

    caretaker.save(state1)
    caretaker.save(state2)

    memento = caretaker.undo()

    assert memento is not None
    assert memento.get_state() == state1


def test_redo():
    caretaker = Caretaker()

    state1 = [{"operation": "add"}]
    state2 = [{"operation": "multiply"}]

    caretaker.save(state1)
    caretaker.save(state2)

    caretaker.undo()
    memento = caretaker.redo()

    assert memento is not None
    assert memento.get_state() == state2

import os
import pandas as pd
from app.history import History


def test_add_and_get_history():
    history = History()
    history.add_record("add", 2, 3, 5)

    df = history.get_history()

    assert len(df) == 1
    assert df.iloc[0]["operation"] == "add"
    assert df.iloc[0]["result"] == 5


def test_clear_history():
    history = History()
    history.add_record("add", 1, 1, 2)
    history.clear()

    df = history.get_history()
    assert df.empty


def test_save_to_csv(tmp_path):
    history = History()
    history.add_record("multiply", 2, 4, 8)

    file_path = tmp_path / "test_history.csv"
    history.save(file_path)

    assert os.path.exists(file_path)

    df = pd.read_csv(file_path)
    assert len(df) == 1
    assert df.iloc[0]["result"] == 8


def test_load_nonexistent_file(tmp_path):
    history = History()
    file_path = tmp_path / "does_not_exist.csv"

    history.load(file_path)

    assert history.get_history().empty

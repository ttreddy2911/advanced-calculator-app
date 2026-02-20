import os
from app.exceptions import ConfigError


class CalculatorConfig:
    def __init__(self):
        self.history_file = os.getenv("HISTORY_FILE")

        if not self.history_file:
            raise ConfigError("HISTORY_FILE environment variable not set")

        self.auto_save = os.getenv("AUTO_SAVE", "false").lower() == "true"

    def get_history_file(self):
        return self.history_file

    def is_auto_save_enabled(self):
        return self.auto_save

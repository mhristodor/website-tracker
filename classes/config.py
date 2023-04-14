from cli import terminal_message as tm
import os


class Config:
    def __init__(self, config: dict) -> None:
        for key in config:
            setattr(self, key, config[key])

        self.path = os.path.abspath(self.path)

    def display(self):
        tm.displayConfig(self)

from cli import terminal_message as tm
import os


class Config:
    def __init__(self, config: dict) -> None:
        for key in config:
            setattr(self, key, config[key])

    def display(self):
        tm.displayConfig(self)

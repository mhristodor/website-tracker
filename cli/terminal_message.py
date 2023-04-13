# from classes.config import Config
from utils.enums import FileError
from utils.enums import TerminalColor

from tabulate import tabulate

import json


def treatFileErrors(err: FileError) -> None:
    print(f"{TerminalColor.ERR.value} {err.value}")


def displayConfig(config) -> None:
    # type of config is Config, did not include the type hint due to circular import
    print(f"{TerminalColor.INFO.value} Current configuration: {config.__dict__}")
    # print(json.dumps(config.__dict__, indent=4))


def fileLoaded() -> None:
    print(f"{TerminalColor.OK.value} {FileError.OK.value}")


def noValidURL() -> None:
    print(f"{TerminalColor.ERR.value} Found no valid website inside the file.")


def validCountURL(file_count: int, valid_count: int) -> None:
    print(
        f"{TerminalColor.INFO.value} Loaded {valid_count} websites from a total of {file_count} lines found."
    )


def mainMessage() -> None:
    print(f"\n{TerminalColor.HEADER.value}Website Tracker{TerminalColor.ENDC.value}\n")


def liveMode() -> None:
    print(f"{TerminalColor.INFO.value} Live mode enabled!")


def displayTable(table) -> None:
    # type of table is Table, did not include the type hint due to circular import
    print(
        f'\n{tabulate(table.table, headers=table.header, tablefmt="outline")}\n',
        end="\r",
    )
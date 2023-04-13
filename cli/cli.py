from cli import parser

from classes.config import Config
from classes.file import FileHandler
from classes.table import Table


def fileOperations(file: FileHandler) -> None:
    file.checkFileExists()
    file.checkFileUTF8()
    file.loadFile()
    file.loadURL()
    file.checkURL()


def cli() -> None:
    args = parser.setupParser()

    config = Config(vars(args))
    config.display()

    file = FileHandler(config.path)

    fileOperations(file)

    table = Table(file.urls)
    table.display()

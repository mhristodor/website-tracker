import os
import codecs

from utils.enums import FileError
from utils.misc import validateURL

from cli import terminal_message as tm


class FileHandler:
    def __init__(self, file_path: str) -> None:
        self.filepath = file_path

    def checkFileUTF8(self) -> None:
        try:
            _ = codecs.open(
                self.filepath, encoding="utf-8", errors="strict"
            ).readlines()
        except UnicodeDecodeError:
            tm.treatFileErrors(FileError.NOT_UTF8)
            quit()

    def checkFileExists(self) -> None:
        if not os.path.isfile(self.filepath):
            tm.treatFileErrors(FileError.NOT_FOUND)
            quit()

    def loadFile(self) -> None:
        with open(self.filepath, "r") as file:
            self.lines = file.readlines()

    def loadURL(self) -> None:
        self.urls = [url.strip() for url in self.lines if validateURL(url.strip())]
        tm.fileLoaded()

    def checkURL(self) -> None:
        if len(self.urls) == 0:
            tm.noValidURL()
            quit()

        tm.validCountURL(len(self.lines), len(self.urls))

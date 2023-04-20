import os
import codecs

from classes.terminal import TerminalMessage

from utils.misc import validateURL

from dataclasses import dataclass, field


@dataclass
class FileHandler:
    """Dataclass with file information.

    It stores information about the file and its contents.
    Performs certain cheks to ensure that the file is vaild
    and the contents are usable by the application.

    Attributes:
        file_path (str): File path.
        lines (list[str]): A list with the lines of the file.
        urls (list[str]): A list with the valid URLs of the file.

    """

    file_path: str = None

    lines: list[str] = field(init=False)
    urls: list[str] = field(init=False)

    def __post_init__(self) -> None:
        self._checkFileExists()
        self._checkFileUTF8()
        self._loadFile()
        self._loadURL()
        self._checkURL()

    def _checkFileUTF8(self) -> None:
        try:
            _ = codecs.open(
                self.file_path, encoding="utf-8", errors="strict"
            ).readlines()
        except UnicodeDecodeError:
            print(TerminalMessage.FILE_NOT_UTF8.value)
            quit()

    def _checkFileExists(self) -> None:
        if not os.path.isfile(self.file_path):
            print(TerminalMessage.FILE_NOT_EXIST.value)
            quit()

    def _loadFile(self) -> None:
        with open(self.file_path, "r") as file:
            self.lines = file.readlines()

    def _loadURL(self) -> None:
        self.urls = [url.strip() for url in self.lines if validateURL(url.strip())]
        print(TerminalMessage.FILE_LOADED.value)

    def _checkURL(self) -> None:
        if len(self.urls) == 0:
            print(TerminalMessage.NO_VALID_URL.value)
            quit()

        print(TerminalMessage.validCountURL(len(self.lines), len(self.urls)))

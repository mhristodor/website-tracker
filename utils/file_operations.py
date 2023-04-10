import os
import codecs
from utils.enums import FileError


def checkFileUTF8(filename: str) -> bool:
    try:
        f = codecs.open(filename, encoding="utf-8", errors="strict").readlines()
    except UnicodeDecodeError:
        return False

    return True


def getUrlsFromFile(filepath: str) -> tuple[list(), FileError]:
    if not os.path.isfile(filepath):
        return ([], FileError.NOT_FOUND)
    if not checkFileUTF8(filepath):
        return ([], FileError.NOT_UTF8)

    with open(filepath, "r") as file:
        return ([url.strip() for url in file.readlines()], FileError.OK)

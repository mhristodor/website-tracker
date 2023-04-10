from enum import Enum


class FileError(Enum):
    NOT_UTF8 = "File is not encoded in UTF-8"
    NOT_FOUND = "File does not exist"
    OK = "OK"

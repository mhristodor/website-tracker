from enum import Enum


class FileError(Enum):
    NOT_UTF8 = "File is not encoded in UTF-8."
    NOT_FOUND = "File does not exist."
    OK = "File loaded successfully."


class TerminalColor(Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    ERR = "\033[91m[FAIL]\033[0m"
    OK = "\033[92m[OK]  \033[0m"
    INFO = "\033[96m[INFO]\033[0m"
    DOWN = "\033[91m[DOWN]\033[0m"
    REDR = "\033[96m[REDR]\033[0m"

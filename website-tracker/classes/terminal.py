from enum import Enum


class TerminalColor(Enum):
    """Enum representing terminal color values.

    It contains predefined status messages and
    color constants.
    """

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
    OK = "\033[92m [OK] \033[0m"
    INFO = "\033[96m[INFO]\033[0m"
    DOWN = "\033[91m[DOWN]\033[0m"
    REDR = "\033[96m[REDR]\033[0m"
    WARN = "\033[93m[WARN]\033[0m"


class TerminalMessage(Enum):
    """Enum containing all terminal messages.

    It contains predefined terminal message values
    and several other methods which return a terminal
    message.
    """

    STARTUP = (
        f"\n{TerminalColor.HEADER.value}Website Tracker{TerminalColor.ENDC.value}\n"
    )

    NO_VALID_URL = f"{TerminalColor.ERR.value} Found no valid website inside the file."

    INCOMPLETE_ARGS = f"{TerminalColor.ERR.value} Argument -m (mail) cannot be used without -l (live) argument."

    LIVE_ENABLED = f"{TerminalColor.INFO.value} Live mode enabled!"

    NO_CREDS = f"{TerminalColor.WARN.value} Credentials file not found. Please input the credentials of the e-mail address the messages will originate from."
    OK_CREDS = f"{TerminalColor.OK.value} Email credentials loaded."

    INPUT_SMTP = f"{TerminalColor.WARN.value} SMTP server: "
    INPUT_EMAIL = f"{TerminalColor.WARN.value} Enter e-mail address: "
    INPUT_PASSWORD = f"{TerminalColor.WARN.value} Enter password: "

    INVALID_SMTP = f"{TerminalColor.ERR.value} SMTP Server is invalid."
    INVALID_CREDS = f"{TerminalColor.ERR.value} Email credentials are invalid."

    FILE_NOT_UTF8 = f"{TerminalColor.ERR.value} File is not encoded in UTF-8."
    FILE_NOT_FOUND = f"{TerminalColor.ERR.value} File does not exist."
    FILE_LOADED = f"{TerminalColor.OK.value} File loaded successfully."

    @classmethod
    def displayConfig(cls, config: dict) -> str:
        """Constructs a message with application configuration.

        Args:
            config (dict): Dictionary containing the configuration.

        Returns:
            message (str): Returns a terminal message with the configuration.

        """
        return f"{TerminalColor.INFO.value} Current configuration: {config}"

    @classmethod
    def validCountURL(cls, file_count: int, valid_count: int) -> str:
        """Constructs a message withthe valid count of URLs.

        Confirmation message of the loaded valid URLs
        compared to the total number of lines in the file.

        Args:
            file_count (int): Number of lines in the file.
            valid_count (int): Number of valid URLs in the file.

        Returns:
           message (str): Returns a formatted terminal message.

        """

        return f"{TerminalColor.INFO.value} Loaded {valid_count} websites from a total of {file_count} lines found."

    @classmethod
    def displayTable(cls, table: str) -> str:
        """Constructs a message with the URLs table.

        Args:
            table (str): String representation of the table.

        Returns:
            message (str): Returns a formatted terminal message with the table.

        """

        return f"\r\n{table}\n\n{TerminalColor.WARNING.value}Use CTRL-C to quit.{TerminalColor.ENDC.value}"

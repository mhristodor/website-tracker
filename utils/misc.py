import re

URL_VALIDATION = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
MAIL_VALIDATION = "^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"


def validateURL(url: str) -> bool:
    """Checks if the given URL is valid.

    Args:
        url (str): Website URL to validate.

    Returns:
        bool: True if matches the regex, False otherwise.
    """
    return re.match(URL_VALIDATION, url) != None


def sanitizeURL(url: str) -> str:
    """Sanitizes the given URL.

    Args:
        url (str): Website URL to sanitize.

    Returns:
        str: Sanitized URL.
    """
    if "https://" in url or "http://" in url:
        return url

    return "https://" + url


def validateMail(email: str) -> bool:
    """Checks if a mail is valid.

    Args:
        email (str): Mail adress to check.

    Returns:
        bool: True if matches the regex, False otherwise.
    """
    return re.match(MAIL_VALIDATION, email) != None


def move(y: int) -> None:
    """Creates the illusion of a live table in terminal.

    Args:
        y (int): Units the pointer to move upwards.
    """
    print(f"\033[{y}A")

import re

URL_VALIDATION = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
MAIL_VALIDATION = "^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"


def validateURL(url: str) -> bool:
    return re.match(URL_VALIDATION, url) != None


def sanitizeURL(url: str) -> str:
    if "https://" in url or "http://" in url:
        return url

    return "https://" + url


def validateMail(email: str) -> bool:
    return re.match(MAIL_VALIDATION, email) != None

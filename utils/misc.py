import re

URL_VALIDATION = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"


def validateURL(url: str) -> bool:
    return re.match(URL_VALIDATION, url) != None

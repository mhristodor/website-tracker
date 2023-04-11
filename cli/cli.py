from cli import file_operations as fo
from utils import misc as misc
from utils.enums import FileError
from utils.enums import TerminalColor
from cli import parser
from utils.classes import WebsiteStatusCheck as wsc
from tabulate import tabulate


def treatFileErrors(err: FileError) -> None:
    match err:
        case FileError.NOT_FOUND:
            print(f"{TerminalColor.ERR.value} {FileError.NOT_FOUND.value}")
            exit()

        case FileError.NOT_UTF8:
            print(f"{TerminalColor.ERR.value} {FileError.NOT_UTF8.value}")
            exit()

        case FileError.OK:
            print(f"{TerminalColor.OK.value} File has been successfully loaded.")


def createTable(websites):
    headers


def cli() -> None:
    args = parser.setupParser()

    website_list, err = fo.getUrlsFromFile(args.path)

    treatFileErrors(err)

    sanitized_website_list = [
        misc.sanitizeURL(url) for url in website_list if misc.validateURL(url)
    ]

    if len(sanitized_website_list) == 0:
        print(f"{TerminalColor.ERR.value} Found no valid website inside the file.")
        exit()
    else:
        print(
            f"{TerminalColor.INFO.value} Loaded {len(sanitized_website_list)} websited from a total of {len(website_list)} lines found."
        )

    websites = [wsc(url) for url in sanitized_website_list]

    if args.live:
        print(f"{TerminalColor.INFO.value} Live mode enabled.")
